"""Fase 6 — Interface interativa (Gradio) para o modelo Random Forest.

O usuário informa seus hábitos com sliders e menus, e o modelo treinado na Fase 2
prevê a produtividade na hora, mostrando também o palpite de cada árvore da floresta.

Uso:
    uv run python 06_app.py          # abre em http://127.0.0.1:7860
    %run 06_app.py                   # dentro de uma célula de notebook (exibe inline)

Pré-requisito: executar 01_eda_preprocessing.ipynb e 02_model_training.ipynb,
que geram models/random_forest.joblib, models/metadata.json e data/train.csv.
"""

import json
import sys
from pathlib import Path

import gradio as gr
import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent
MODEL_DIR = RAIZ / "models"
DATA_DIR = RAIZ / "data"

SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, BLUE_L, ORANGE = "#2a78d6", "#9ec5f4", "#eb6834"

GENEROS = {"Feminino": "Female", "Masculino": "Male", "Outro": "Other"}
AREAS = {"Educação": "Education", "Finanças": "Finance", "Saúde": "Health", "TI": "IT",
         "Estudante": "Student", "Desempregado(a)": "Unemployed"}
REDES = {r: r for r in ["Facebook", "Instagram", "Telegram", "TikTok", "Twitter"]}


def carregar_artefatos():
    faltando = [p for p in (MODEL_DIR / "random_forest.joblib", MODEL_DIR / "metadata.json",
                            DATA_DIR / "train.csv") if not p.exists()]
    if faltando:
        sys.exit("Arquivos não encontrados: " + ", ".join(str(p.relative_to(RAIZ)) for p in faltando)
                 + "\nExecute antes os notebooks 01_eda_preprocessing.ipynb e 02_model_training.ipynb.")
    metadados = json.loads((MODEL_DIR / "metadata.json").read_text())
    modelo = joblib.load(MODEL_DIR / "random_forest.joblib")
    # Para prever uma pessoa por vez, o paralelismo custa mais do que economiza (~4x mais lento)
    modelo.n_jobs = 1
    alvo_treino = pd.read_csv(DATA_DIR / "train.csv", usecols=[metadados["alvo"]])[metadados["alvo"]].to_numpy()
    return modelo, metadados["features"], np.sort(alvo_treino)


MODELO, FEATURES, ALVO_TREINO = carregar_artefatos()
MEDIA_GERAL = ALVO_TREINO.mean()

# Ordem dos componentes de entrada = ordem dos argumentos de prever()
CAMPOS = [
    "daily_social_media_time", "social_platform_preference", "number_of_notifications",
    "screen_time_before_sleep", "weekly_offline_hours", "uses_focus_apps", "has_digital_wellbeing_enabled",
    "job_satisfaction_score", "job_type", "work_hours_per_day", "breaks_during_work",
    "coffee_consumption_per_day", "sleep_hours", "stress_level", "days_feeling_burnout_per_month",
    "age", "gender",
]


def montar_linha(valores):
    """Converte os valores da interface em uma linha no formato das features do modelo (one-hot)."""
    v = dict(zip(CAMPOS, valores))
    linha = {f: 0.0 for f in FEATURES}
    for campo, valor in v.items():
        if campo == "gender":
            linha[f"gender_{GENEROS[valor]}"] = 1.0
        elif campo == "job_type":
            linha[f"job_{AREAS[valor]}"] = 1.0
        elif campo == "social_platform_preference":
            linha[f"platform_{REDES[valor]}"] = 1.0
        else:
            linha[campo] = float(valor)
    return pd.DataFrame([linha], columns=FEATURES)


def palpites_das_arvores(X):
    """Previsão de cada árvore da floresta para cada linha de X (matriz árvores × linhas)."""
    Xv = X.to_numpy()
    return np.stack([arvore.predict(Xv) for arvore in MODELO.estimators_])


def fmt(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


def cartao_resultado(previsao, palpites):
    percentil = np.searchsorted(ALVO_TREINO, previsao) / len(ALVO_TREINO) * 100
    p10, p90 = np.percentile(palpites, [10, 90])
    if previsao < 3.5:
        faixa, cor = "Baixa", "#d03b3b"
    elif previsao < 6.5:
        faixa, cor = "Média", "#c98500"
    else:
        faixa, cor = "Alta", "#0ca30c"
    diferenca = previsao - MEDIA_GERAL
    sinal = "acima" if diferenca >= 0 else "abaixo"
    return f"""
<div class="cartao">
  <div class="rotulo">Produtividade prevista</div>
  <div class="numero">{fmt(previsao)}<span class="escala"> / 10</span></div>
  <div class="faixa" style="color:{cor}">&#9679; Produtividade {faixa.lower()}</div>
  <div class="detalhes">
    <div><b>{fmt(abs(diferenca))}</b> ponto {sinal} da média do dataset ({fmt(MEDIA_GERAL)})</div>
    <div>Mais produtivo(a) que <b>{percentil:.0f}%</b> das pessoas do treino</div>
    <div>80% das {len(palpites)} árvores preveem entre <b>{fmt(p10)}</b> e <b>{fmt(p90)}</b></div>
  </div>
</div>
"""


def grafico_arvores(previsao, palpites):
    fig, ax = plt.subplots(figsize=(6.4, 2.6), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    ax.hist(palpites, bins=np.linspace(0, 10, 41), color=BLUE_L, edgecolor=SURFACE)
    ax.axvline(previsao, color=ORANGE, lw=2.5, label=f"consenso (média) = {fmt(previsao)}")
    ax.set_xlim(0, 10)
    ax.set_yticks([])
    ax.set_xlabel("Palpite de cada árvore", color=INK_2)
    ax.set_title(f"O palpite das {len(palpites)} árvores da floresta", loc="left", fontsize=11,
                 fontweight="bold", color=INK)
    ax.legend(frameon=False, loc="upper left", fontsize=9)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color(INK_2)
    ax.tick_params(colors=INK_2)
    fig.tight_layout()
    plt.close(fig)
    return fig


def grafico_e_se(linha):
    """Curvas 'e se?': como a previsão desta pessoa muda variando uma variável e mantendo o resto."""
    fig, ax = plt.subplots(figsize=(6.4, 3.2), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for col, cor, rotulo, maximo in [
        ("daily_social_media_time", BLUE, "Horas/dia em redes sociais (0 a 12)", 12),
        ("job_satisfaction_score", ORANGE, "Satisfação com o trabalho (0 a 10)", 10),
    ]:
        grade = np.linspace(0, maximo, 25)
        X = pd.concat([linha] * len(grade), ignore_index=True)
        X[col] = grade
        ax.plot(grade / maximo * 100, MODELO.predict(X), color=cor, lw=2.5, label=rotulo)
        atual = linha[col].iloc[0]
        ax.scatter([atual / maximo * 100], MODELO.predict(linha), color=cor, s=60, zorder=3,
                   edgecolor=SURFACE, linewidth=1.5)
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 50, 100], ["mínimo", "meio", "máximo"])
    ax.set_ylabel("Produtividade prevista", color=INK_2)
    ax.set_title("E se você mudasse só uma coisa? (ponto = você agora)", loc="left", fontsize=11,
                 fontweight="bold", color=INK)
    ax.legend(frameon=False, loc="upper left", fontsize=9)
    ax.grid(color=GRID, lw=0.6)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(colors=INK_2)
    fig.tight_layout()
    plt.close(fig)
    return fig


def prever(*valores):
    linha = montar_linha(valores)
    palpites = palpites_das_arvores(linha)[:, 0]
    previsao = palpites.mean()  # igual a MODELO.predict(linha): a floresta faz a média das árvores
    return cartao_resultado(previsao, palpites), grafico_arvores(previsao, palpites), grafico_e_se(linha)


CSS = """
.cartao { background: #ffffff; border: 1px solid #e4e3df; border-radius: 14px; padding: 22px 26px; }
.cartao .rotulo { color: #52514e; font-size: 15px; text-transform: uppercase; letter-spacing: .05em; }
.cartao .numero { font-size: 64px; font-weight: 700; color: #0b0b0b; line-height: 1.1; }
.cartao .escala { font-size: 26px; color: #52514e; font-weight: 400; }
.cartao .faixa { font-size: 18px; font-weight: 600; margin: 4px 0 14px; }
.cartao .detalhes { color: #52514e; font-size: 15px; line-height: 1.8; border-top: 1px solid #e4e3df; padding-top: 10px; }
.cartao b { color: #0b0b0b; }
#titulo h1 { margin-bottom: 0; }
"""

# Os gráficos e o cartão são claros: força o tema claro mesmo se o sistema estiver no modo escuro
FORCAR_TEMA_CLARO = """
<script>
const url = new URL(window.location);
if (url.searchParams.get("__theme") !== "light") {
  url.searchParams.set("__theme", "light");
  window.location.replace(url);
}
</script>
"""

TEMA = gr.themes.Soft(primary_hue="blue", neutral_hue="stone",
                      font=[gr.themes.GoogleFont("Inter"), "Segoe UI", "sans-serif"])


def criar_app():
    with gr.Blocks(title="Produtividade vs Redes Sociais — Random Forest") as app:
        gr.Markdown(
            "# Qual é a sua produtividade?\n"
            "Ajuste os seus hábitos e veja na hora a produtividade prevista por um **Random Forest** "
            "de 300 árvores, treinado com 22 mil pessoas do dataset *Social Media vs Productivity*.",
            elem_id="titulo",
        )
        with gr.Row(equal_height=False):
            with gr.Column(scale=5):
                with gr.Tab("Hábitos digitais"):
                    redes = gr.Slider(0, 12, value=3, step=0.5, label="Horas por dia em redes sociais")
                    plataforma = gr.Dropdown(list(REDES), value="Instagram", label="Rede social favorita")
                    notificacoes = gr.Slider(30, 90, value=60, step=1, label="Notificações por dia")
                    tela = gr.Slider(0, 3, value=1, step=0.25, label="Horas de tela antes de dormir")
                    offline = gr.Slider(0, 40, value=10, step=1, label="Horas offline por semana")
                    with gr.Row():
                        foco = gr.Checkbox(value=False, label="Uso apps de foco")
                        bem_estar = gr.Checkbox(value=False, label="Bem-estar digital ativado")
                with gr.Tab("Trabalho"):
                    satisfacao = gr.Slider(0, 10, value=5, step=0.5, label="Satisfação com o trabalho",
                                           info="A variável que o modelo considera mais importante")
                    area = gr.Dropdown(list(AREAS), value="TI", label="Área de atuação")
                    horas = gr.Slider(0, 12, value=7, step=0.5, label="Horas de trabalho por dia")
                    pausas = gr.Slider(0, 10, value=5, step=1, label="Pausas durante o trabalho")
                    cafe = gr.Slider(0, 10, value=2, step=1, label="Xícaras de café por dia")
                with gr.Tab("Bem-estar e perfil"):
                    sono = gr.Slider(3, 10, value=6.5, step=0.5, label="Horas de sono")
                    estresse = gr.Slider(1, 10, value=6, step=1, label="Nível de estresse")
                    burnout = gr.Slider(0, 31, value=16, step=1, label="Dias com sensação de burnout no mês")
                    idade = gr.Slider(18, 65, value=30, step=1, label="Idade")
                    genero = gr.Dropdown(list(GENEROS), value="Feminino", label="Gênero")

            with gr.Column(scale=6):
                cartao = gr.HTML()
                grafico_floresta = gr.Plot(show_label=False)
                grafico_cenarios = gr.Plot(show_label=False)

        entradas = [redes, plataforma, notificacoes, tela, offline, foco, bem_estar, satisfacao, area, horas,
                    pausas, cafe, sono, estresse, burnout, idade, genero]
        assert len(entradas) == len(CAMPOS)
        saidas = [cartao, grafico_floresta, grafico_cenarios]

        gr.Examples(
            label="Perfis prontos (clique para carregar)",
            examples=[
                [3, "Instagram", 60, 1, 10, False, False, 5, "TI", 7, 5, 2, 6.5, 6, 16, 30, "Feminino"],
                [10, "TikTok", 85, 2.5, 1, False, False, 5, "Estudante", 6, 3, 4, 5, 8, 25, 21, "Masculino"],
                [1, "Telegram", 40, 0, 30, True, True, 5, "Saúde", 8, 6, 1, 8, 3, 4, 45, "Feminino"],
                [4, "Twitter", 65, 1.5, 8, False, False, 9, "Finanças", 9, 4, 3, 6, 7, 12, 38, "Outro"],
                [4, "Facebook", 65, 1.5, 8, False, False, 1.5, "Educação", 7, 5, 2, 7, 4, 20, 50, "Masculino"],
            ],
            example_labels=["Perfil médio", "Muito conectado", "Detox digital", "Muito satisfeito",
                            "Pouco satisfeito"],
            inputs=entradas,
            outputs=saidas,
            fn=prever,
            run_on_click=True,
            cache_examples=False,
        )

        gr.Markdown(
            "**Como ler:** a previsão é a **média dos palpites das 300 árvores** (o consenso da floresta). "
            "Experimente arrastar o slider de redes sociais e depois o de satisfação com o trabalho: neste "
            "dataset, o modelo aprendeu que só a satisfação move a produtividade. *Os dados são sintéticos e "
            "o modelo mostra associações, não causas.*"
        )

        # "input" dispara só com interação do usuário (não quando um perfil pronto altera os campos, que já
        # recalcula uma única vez pelo Examples). always_last: ao arrastar um slider, processa só o último valor
        gr.on(triggers=[c.input for c in entradas] + [app.load], fn=prever, inputs=entradas, outputs=saidas,
              trigger_mode="always_last")
    return app


app = criar_app()

if __name__ == "__main__":
    app.launch(theme=TEMA, css=CSS, head=FORCAR_TEMA_CLARO)

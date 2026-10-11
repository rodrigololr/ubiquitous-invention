"""Gera os diagramas didáticos usados em 05_slides.md (salvos em slides/img/).

Uso: uv run python slides/diagramas.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).parent / "img"
OUT.mkdir(exist_ok=True)

SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, BLUE_L, BLUE_XL = "#2a78d6", "#9ec5f4", "#cde2fb"
ORANGE, ORANGE_L = "#eb6834", "#fbd5c4"
MUTED = "#b9b8b2"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.size": 14,
    "text.color": INK,
})


def tela(w=12, h=6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def caixa(ax, x, y, w, h, texto, cor=BLUE, cor_texto="white", fs=14, peso="bold"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor=cor, edgecolor="none"))
    ax.text(x, y, texto, ha="center", va="center", color=cor_texto, fontsize=fs, fontweight=peso)


def seta(ax, x0, y0, x1, y1, cor=INK_2, texto=None, lw=2):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=18, color=cor, lw=lw))
    if texto:
        ax.text((x0 + x1) / 2 + 0.15, (y0 + y1) / 2, texto, color=INK_2, fontsize=12, ha="left", va="center")


def salvar(fig, nome, recortar=True):
    # recortar=False mantém o mesmo enquadramento entre imagens de uma sequência progressiva
    fig.savefig(OUT / f"{nome}.png", dpi=150, bbox_inches="tight" if recortar else None, pad_inches=0.15)
    plt.close(fig)


def circulos():
    fig, ax = tela(10, 7)
    for r, cor, borda, rotulo, y_txt in [
        (3.3, BLUE_XL, BLUE, "Inteligência Artificial", 6.25),
        (2.2, BLUE_L, BLUE, "Machine Learning", 5.1),
        (1.05, BLUE, BLUE, "Deep Learning", 3.5),
    ]:
        ax.add_patch(Circle((5, 3.4), r, facecolor=cor, edgecolor=borda, lw=2))
        ax.text(5, y_txt, rotulo, ha="center", va="center", fontsize=17, fontweight="bold",
                color="white" if cor == BLUE else INK)
    ax.add_patch(Circle((3.6, 2.75), 0.16, color=ORANGE))
    ax.text(3.6, 2.2, "Random Forest", ha="center", fontsize=14, fontweight="bold", color=ORANGE)
    salvar(fig, "ia_ml_dl")


def programacao_vs_ml():
    fig, ax = tela(13, 5)
    ax.text(3.2, 4.6, "Programação tradicional", ha="center", fontsize=18, fontweight="bold")
    caixa(ax, 1.4, 3.2, 2.0, 0.9, "Regras", MUTED, INK)
    caixa(ax, 1.4, 1.8, 2.0, 0.9, "Dados", MUTED, INK)
    caixa(ax, 4.9, 2.5, 2.2, 1.0, "Respostas", BLUE)
    seta(ax, 2.5, 3.0, 3.7, 2.6)
    seta(ax, 2.5, 2.0, 3.7, 2.4)
    ax.text(3.2, 0.7, "um humano escreve as regras", ha="center", fontsize=13, color=INK_2, style="italic")

    ax.plot([6.5, 6.5], [0.4, 4.8], color=GRID, lw=2)

    ax.text(9.8, 4.6, "Machine Learning", ha="center", fontsize=18, fontweight="bold", color=ORANGE)
    caixa(ax, 8.0, 3.2, 2.0, 0.9, "Dados", MUTED, INK)
    caixa(ax, 8.0, 1.8, 2.0, 0.9, "Respostas", MUTED, INK)
    caixa(ax, 11.5, 2.5, 2.2, 1.0, "Regras", ORANGE)
    seta(ax, 9.1, 3.0, 10.3, 2.6)
    seta(ax, 9.1, 2.0, 10.3, 2.4)
    ax.text(9.8, 0.7, "a máquina descobre as regras", ha="center", fontsize=13, color=INK_2, style="italic")
    salvar(fig, "programacao_vs_ml")


def divisao_treino_teste():
    fig, ax = tela(12, 2.6)
    ax.add_patch(Rectangle((0.2, 1.0), 9.2, 0.9, color=BLUE))
    ax.add_patch(Rectangle((9.45, 1.0), 2.35, 0.9, color=ORANGE))
    ax.text(4.8, 1.45, "Treino: 80% (22.108 pessoas)", ha="center", va="center", color="white",
            fontsize=16, fontweight="bold")
    ax.text(10.62, 1.45, "Teste: 20%", ha="center", va="center", color="white", fontsize=16, fontweight="bold")
    ax.text(4.8, 0.55, "o material de estudo", ha="center", fontsize=13, color=INK_2, style="italic")
    ax.text(10.62, 0.55, "a prova inédita", ha="center", fontsize=13, color=INK_2, style="italic")
    salvar(fig, "treino_teste")


def arvore_simples(etapa):
    # etapa 1: só a pergunta; 2: com galhos; 3: com folhas
    fig, ax = tela(10, 5.5)
    caixa(ax, 5, 4.6, 6.4, 1.0, "Satisfação com o trabalho > 5?", ORANGE, fs=16)
    if etapa >= 2:
        seta(ax, 4.0, 4.05, 2.4, 2.75)
        seta(ax, 6.0, 4.05, 7.6, 2.75)
        ax.text(2.7, 3.55, "Não", fontsize=15, fontweight="bold", color=INK_2)
        ax.text(6.95, 3.55, "Sim", fontsize=15, fontweight="bold", color=INK_2)
    if etapa >= 3:
        caixa(ax, 2.2, 2.1, 3.4, 1.15, "Produtividade\nprevista: 3,8", BLUE, fs=15)
        caixa(ax, 7.8, 2.1, 3.4, 1.15, "Produtividade\nprevista: 6,4", BLUE, fs=15)
        ax.text(5, 0.7, "primeira pergunta escolhida pelo algoritmo nos nossos dados", ha="center",
                fontsize=12, color=INK_2, style="italic")
    salvar(fig, f"arvore_{etapa}", recortar=False)


def arvore_grande():
    fig, ax = tela(12, 6)
    rng = np.random.default_rng(3)
    perguntas = ["Satisfação > 5?", "Satisfação > 3?", "Satisfação > 7?", "Idade > 40?", "Sono > 6h?",
                 "Café > 2?", "Pausas > 4?"]
    niveis = 6
    for nivel in range(niveis):
        n = 2 ** nivel
        y = 5.4 - nivel * 0.95
        xs = np.linspace(0.3, 11.7, n + 2)[1:-1] if n > 1 else [6.0]
        for i, x in enumerate(xs):
            if nivel < niveis - 1:
                filhos_y = y - 0.95
                n_f = 2 ** (nivel + 1)
                xs_f = np.linspace(0.3, 11.7, n_f + 2)[1:-1]
                for xf in xs_f[2 * i:2 * i + 2]:
                    ax.plot([x, xf], [y, filhos_y], color=MUTED, lw=1, zorder=0)
            if nivel <= 2:
                rotulo = perguntas[min(2 ** nivel - 1 + i, len(perguntas) - 1)]
                w = 2.4 if nivel < 2 else 2.0
                caixa(ax, x, y, w, 0.55, rotulo, ORANGE if nivel == 0 else BLUE, fs=11 if nivel < 2 else 10)
            elif nivel < niveis - 1:
                ax.add_patch(Circle((x, y), 0.13, color=BLUE))
            else:
                ax.add_patch(Circle((x, y), 0.09, color=BLUE_L))
    ax.text(6, 0.25, "... e continua até cada folha ter uma única pessoa (22.108 folhas)", ha="center",
            fontsize=13, color=INK_2, style="italic")
    salvar(fig, "arvore_grande")


def multidao():
    rng = np.random.default_rng(7)
    real = 500
    chutes = rng.lognormal(np.log(real), 0.35, 400)
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.hist(chutes, bins=40, color=BLUE_L, edgecolor=SURFACE)
    ax.axvline(real, color=INK, lw=2.5)
    ax.axvline(312, color=MUTED, lw=2, ls="--")
    ax.axvline(chutes.mean(), color=ORANGE, lw=3, ls="--")
    topo = ax.get_ylim()[1]
    ax.text(real + 18, topo * 0.95, f"valor real: {real}", fontsize=13, fontweight="bold", va="top")
    ax.text(312 - 8, topo * 0.95, "um chute: 312", fontsize=13, color=INK_2, ha="right", va="top")
    ax.text(chutes.mean() + 18, topo * 0.78, f"média de 400 chutes: {chutes.mean():.0f}", fontsize=13,
            color=ORANGE, fontweight="bold", va="top")
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.set_yticks([])
    ax.set_xlabel("Quantas balas tem no pote?", fontsize=13)
    ax.set_facecolor(SURFACE)
    salvar(fig, "sabedoria_multidoes")


def bootstrap():
    rng = np.random.default_rng(11)
    fig, ax = tela(13, 5.6)
    n = 10
    ax.text(7.3, 5.75, "sorteio com reposição: tons claros = pessoas repetidas", ha="center", fontsize=12,
            color=INK_2, style="italic")
    ax.text(1.3, 5.25, "Treino", ha="center", fontsize=15, fontweight="bold")
    for i in range(n):
        ax.add_patch(Rectangle((0.6, 4.6 - i * 0.42), 1.4, 0.36, color=BLUE))
        ax.text(1.3, 4.78 - i * 0.42, f"pessoa {i + 1}", ha="center", va="center", color="white", fontsize=10)
    for k, x0 in enumerate([4.0, 7.3, 10.6]):
        amostra = rng.integers(0, n, n)
        ax.text(x0 + 0.7, 5.25, f"Árvore {k + 1}", ha="center", fontsize=15, fontweight="bold", color=ORANGE)
        for j, idx in enumerate(sorted(amostra)):
            repetida = (amostra == idx).sum() > 1
            ax.add_patch(Rectangle((x0, 4.6 - j * 0.42), 1.4, 0.36, color=BLUE_L if repetida else BLUE))
            ax.text(x0 + 0.7, 4.78 - j * 0.42, f"pessoa {idx + 1}", ha="center", va="center",
                    color=INK if repetida else "white", fontsize=10)
        fora = sorted(set(range(n)) - set(amostra))
        ax.text(x0 + 0.7, 0.15, "fora: " + ", ".join(str(f + 1) for f in fora), ha="center", fontsize=11,
                color=INK_2)
    salvar(fig, "bootstrap")


def sorteio_features():
    rng = np.random.default_rng(5)
    fig, ax = tela(12, 4.2)
    sorteadas = set(rng.choice(28, 14, replace=False))
    for i in range(28):
        x = 0.5 + (i % 14) * 0.8
        y = 2.9 if i < 14 else 1.9
        cor = ORANGE if i in sorteadas else GRID
        ax.add_patch(FancyBboxPatch((x, y), 0.62, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=cor, edgecolor="none"))
    ax.text(6, 4.0, "28 variáveis disponíveis", ha="center", fontsize=15, fontweight="bold")
    ax.text(6, 1.2, "em cada pergunta, a árvore só pode escolher entre as 14 sorteadas (laranja)",
            ha="center", fontsize=13, color=INK_2, style="italic")
    salvar(fig, "sorteio_features")


def consenso():
    fig, ax = tela(13, 5.5)
    caixa(ax, 1.3, 2.75, 2.0, 1.2, "Pessoa\nnova", INK_2, fs=15)
    palpites = ["5,2", "6,1", "5,7", "4,9", "5,9"]
    ys = [4.8, 3.8, 2.75, 1.7, 0.7]
    for p, y in zip(palpites, ys):
        seta(ax, 2.4, 2.75, 4.0, y, cor=MUTED, lw=1.2)
        caixa(ax, 4.9, y, 1.6, 0.7, "Árvore", BLUE, fs=13)
        ax.text(6.05, y, f"→  {p}", va="center", fontsize=15, color=INK)
    ax.text(4.9, 0.05, "... × 300 árvores", ha="center", fontsize=12, color=INK_2, style="italic")
    seta(ax, 7.4, 2.75, 8.9, 2.75, cor=INK_2)
    caixa(ax, 10.9, 2.75, 3.6, 1.6, "Média dos\n300 palpites\n= 5,6", ORANGE, fs=17)
    salvar(fig, "consenso")


def pipeline():
    fig, ax = tela(14, 2.6)
    etapas = ["Exploração", "Limpeza", "Treino", "Avaliação", "Insights", "Interface"]
    for i, e in enumerate(etapas):
        x = 1.15 + i * 2.35
        caixa(ax, x, 1.4, 1.95, 1.0, e, ORANGE if e == "Interface" else BLUE, fs=14)
        ax.text(x, 0.55, f"Fase {i + 1}", ha="center", fontsize=11, color=INK_2)
        if i < len(etapas) - 1:
            seta(ax, x + 1.0, 1.4, x + 1.35, 1.4)
    salvar(fig, "pipeline")


if __name__ == "__main__":
    circulos()
    programacao_vs_ml()
    divisao_treino_teste()
    for etapa in (1, 2, 3):
        arvore_simples(etapa)
    arvore_grande()
    multidao()
    bootstrap()
    sorteio_features()
    consenso()
    pipeline()
    print(f"Diagramas salvos em {OUT}: {sorted(p.name for p in OUT.glob('*.png'))}")

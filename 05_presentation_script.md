# Roteiro dos Slides — Aprendizado de Máquina via Algoritmo Random Forest

**Disciplina:** Inteligência Artificial
**Tema:** Aprendizado de Máquina via Algoritmo Random Forest
**Estudo de caso:** Redes Sociais vs Produtividade
**Duração sugerida:** 18 a 22 minutos, mais a demonstração e as perguntas

---

## Como ler este roteiro

Cada slide segue a lógica **"clique para aparecer"**: o conteúdo é revelado aos poucos, para que a turma acompanhe uma ideia de cada vez.

| Marcação | Significado |
|---|---|
| **[Inicial]** | O que aparece assim que o slide abre |
| **[Clique 1]**, **[Clique 2]**... | Elemento revelado a cada clique, em ordem |
| **Visual** | Imagem, diagrama ou gráfico sugerido (os arquivos estão em `figures/`) |
| **Fala** | Sugestão do que dizer. Não é para ler: é um guia do raciocínio |

Recomendações gerais de design:

- Pouco texto por tela: no máximo 3 a 4 linhas curtas visíveis ao mesmo tempo.
- Fundo claro e uma única cor de destaque (laranja) para o "elemento que importa". Os gráficos do projeto já seguem essa convenção: laranja = satisfação com o trabalho, azul = demais variáveis.
- Animação de entrada simples ("Aparecer" ou "Esmaecer"), sem efeitos chamativos.

### Mapa da apresentação

| Bloco | Slides | Tempo |
|---|---|---|
| Abertura | 1 | 0,5 min |
| 1. Introdução à IA | 2 a 4 | 2,5 min |
| 2. Mergulho em Machine Learning | 5 a 8 | 3,5 min |
| 3. Random Forest | 9 a 16 | 5 min |
| 4. O Projeto | 17 a 21 | 3 min |
| 5. Descobertas | 22 a 28 | 4,5 min |
| 6. Encerramento | 29 a 30 | 1 min + demonstração |

---

## Abertura

### Slide 1 — Capa

- **[Inicial]** Título: *Aprendizado de Máquina via Algoritmo Random Forest*
- **[Inicial]** Subtítulo: *Estudo de caso: redes sociais derrubam a nossa produtividade?*
- **[Inicial]** Nomes dos integrantes, disciplina e data

**Visual:** ilustração minimalista de uma floresta estilizada em que cada árvore é um pequeno diagrama de decisão.

**Fala:** "Hoje vamos mostrar como uma máquina aprende com dados usando um algoritmo chamado Random Forest. E vamos usar uma pergunta que todo mundo aqui já se fez: será que o tempo que a gente passa nas redes sociais está acabando com a nossa produtividade?"

---

## Bloco 1 — Introdução à Inteligência Artificial

### Slide 2 — O que é Inteligência Artificial?

- **[Inicial]** Pergunta grande no centro: *"O que é Inteligência Artificial?"*
- **[Clique 1]** Definição: *Área da computação que cria sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana.*
- **[Clique 2]** Quatro ícones aparecem lado a lado: **reconhecer** (rostos, voz), **entender** (textos, perguntas), **decidir** (rotas, recomendações), **prever** (clima, demanda)
- **[Clique 3]** Rodapé: *Você usa IA várias vezes por dia: o feed da sua rede social é organizado por uma.*

**Fala:** "IA não é só robô de filme. É qualquer sistema que faz algo que pareceria exigir inteligência. E a ironia: o próprio feed das redes sociais que vamos estudar é montado por uma IA."

### Slide 3 — Uma linha do tempo rápida

- **[Inicial]** Linha do tempo horizontal vazia
- **[Clique 1]** **1950:** Alan Turing pergunta *"As máquinas podem pensar?"*
- **[Clique 2]** **1956:** o termo *Inteligência Artificial* é cunhado na conferência de Dartmouth
- **[Clique 3]** **Anos 1980–90:** sistemas especialistas (regras escritas à mão) e o crescimento do Machine Learning
- **[Clique 4]** **2001:** Leo Breiman publica o **Random Forest**, o algoritmo de hoje
- **[Clique 5]** **Hoje:** assistentes de IA, carros autônomos, diagnóstico por imagem

**Fala:** "A ideia é antiga. O que mudou foi a quantidade de dados e de poder de computação. Repare que o Random Forest tem mais de 20 anos e continua sendo um dos algoritmos mais usados em dados tabulares."

### Slide 4 — Onde entra o Machine Learning?

- **[Inicial]** Um círculo grande: **Inteligência Artificial**
- **[Clique 1]** Um círculo dentro dele: **Machine Learning**, com a legenda *"sistemas que aprendem com exemplos, em vez de seguir regras escritas à mão"*
- **[Clique 2]** Um círculo menor ainda: **Deep Learning**, com a legenda *"redes neurais com muitas camadas"*
- **[Clique 3]** Uma seta aponta para a região de Machine Learning: *"O Random Forest mora aqui"*

**Visual:** três círculos concêntricos.

**Fala:** "Machine Learning é uma subárea da IA. Em vez de um programador escrever todas as regras, a máquina descobre as regras olhando exemplos. O Random Forest é um algoritmo clássico de Machine Learning, não de Deep Learning."

---

## Bloco 2 — Mergulho em Machine Learning

### Slide 5 — Programar vs ensinar

- **[Inicial]** Lado esquerdo, título *Programação tradicional*: `Regras + Dados → Respostas`
- **[Clique 1]** Exemplo: *"SE a pessoa usa mais de 5 h de rede social, ENTÃO é pouco produtiva"*. Alguém precisou inventar essa regra.
- **[Clique 2]** Lado direito, título *Machine Learning*: `Dados + Respostas → Regras`
- **[Clique 3]** Exemplo: *"Aqui estão 22 mil pessoas e a produtividade de cada uma. Descubra sozinho o que importa."*

**Fala:** "Essa é a virada de chave. No Machine Learning a gente inverte o processo: entrega exemplos com as respostas certas, e o algoritmo descobre as regras. Guardem esse exemplo da esquerda. No final vamos ver se a regra que a gente 'acha' que é verdade sobrevive aos dados."

### Slide 6 — Como a máquina aprende: features e alvo

- **[Inicial]** Uma linha de tabela representando uma pessoa: *idade 32, 4 h/dia de redes sociais, 60 notificações, 7 h de sono, satisfação 6...*
- **[Clique 1]** As colunas de entrada ficam azuis, com o rótulo **Features (o que sabemos)**
- **[Clique 2]** A última coluna fica laranja, com o rótulo **Alvo (o que queremos prever)**: *produtividade = 5,8*
- **[Clique 3]** A linha se multiplica em milhares de linhas, com a frase *"O algoritmo procura padrões que ligam as features ao alvo"*

**Fala:** "Cada pessoa é um exemplo. As características são as features, e o que queremos prever é o alvo. Com milhares de exemplos, o algoritmo encontra padrões que se repetem."

### Slide 7 — Que tipo de pergunta estamos fazendo?

- **[Inicial]** Título: *Aprendizado supervisionado: temos as respostas certas para aprender*
- **[Clique 1]** **Classificação:** prever uma categoria. *"Esse e-mail é spam ou não?"*
- **[Clique 2]** **Regressão:** prever um número. *"Qual a produtividade desta pessoa, de 0 a 10?"*
- **[Clique 3]** Um destaque circula a Regressão: *"Nosso caso: o alvo é um número contínuo. Dividir em 'baixa / média / alta' jogaria informação fora."*

**Fala:** "Como a produtividade é uma nota com casas decimais, usamos regressão. Se dividíssemos em faixas, uma pessoa com 4,9 e outra com 5,1 cairiam em classes diferentes, e isso não faz sentido."

### Slide 8 — Treino e teste: a prova com questões inéditas

- **[Inicial]** Uma barra representando os 27 mil registros
- **[Clique 1]** A barra se divide: **80% treino** (azul), com o rótulo *"o material de estudo"*
- **[Clique 2]** **20% teste** (laranja), com o rótulo *"a prova, com questões que o modelo nunca viu"*
- **[Clique 3]** Alerta: **Overfitting = decorar a matéria.** Tira 10 nos exercícios e vai mal na prova.

**Fala:** "O jeito honesto de avaliar um modelo é como uma prova: com perguntas que ele nunca viu. Um modelo que só decorou o treino é inútil. Esse conceito de 'decorar' vai ser o vilão do próximo bloco."

---

## Bloco 3 — Random Forest, passo a passo

> Este é o coração da apresentação. Cada slide adiciona **uma** peça à explicação.

### Slide 9 — Peça 1: uma Árvore de Decisão

- **[Inicial]** Uma única caixa no topo: *"Satisfação com o trabalho > 5?"*
- **[Clique 1]** Dois galhos saem dela: **Sim** e **Não**
- **[Clique 2]** No galho *Não*, uma folha: *"Produtividade prevista: 3,8"*
- **[Clique 3]** No galho *Sim*, outra folha: *"Produtividade prevista: 6,4"*

**Visual:** diagrama de árvore simples, com a pergunta em laranja e as folhas em azul.

**Fala:** "Uma árvore de decisão é um jogo de perguntas de sim ou não. Cada pergunta divide as pessoas em grupos mais parecidos entre si, e no final cada grupo recebe uma previsão, que é a média do grupo. E esta não é uma árvore inventada: treinando com os nossos dados, a primeira pergunta que o algoritmo escolhe sozinho é exatamente essa, com esses valores."

### Slide 10 — A árvore cresce

- **[Inicial]** A mesma árvore do slide anterior
- **[Clique 1]** Cada folha vira uma nova pergunta: *"Satisfação > 7?"*, *"Idade > 40?"*, *"Horas de sono > 6?"*
- **[Clique 2]** Mais níveis aparecem, até a árvore ficar enorme e difícil de ler
- **[Clique 3]** Legenda: *"No nosso projeto, uma árvore sem limite chegou a 22.108 folhas: uma para cada pessoa do treino."*

**Fala:** "O algoritmo escolhe sozinho qual pergunta fazer em cada passo: aquela que mais reduz o erro. E ele continua perguntando, perguntando... até cada folha ter uma única pessoa."

### Slide 11 — Peça 2: o problema da árvore única

- **[Inicial]** Título: *"Uma árvore sozinha decora"*
- **[Clique 1]** Barra azul enorme: **R² no treino = 1,00**, com a legenda *"acertou 100% do que estudou"*
- **[Clique 2]** Barra laranja bem menor: **R² em dados novos = 0,41**, com a legenda *"foi mal na prova"*
- **[Clique 3]** Conclusão: *"Árvores únicas são instáveis: mudar poucos dados muda a árvore inteira."*

**Visual:** apenas a primeira linha do gráfico `figures/02_arvore_vs_floresta.png`, recortada.

**Fala:** "Aqui está o overfitting na prática, com os nossos dados. A árvore decorou o treino. Cada folha dela aprendeu o ruído de poucas pessoas específicas, e isso não se repete em pessoas novas."

### Slide 12 — A ideia: sabedoria das multidões

- **[Inicial]** Um pote de balas: *"Quantas balas tem aqui?"*
- **[Clique 1]** Um chute individual: *"312"*, longe do valor real
- **[Clique 2]** Centenas de chutes aparecem; muitos erram para cima e muitos para baixo
- **[Clique 3]** **Média de todos os chutes: muito perto do valor real**
- **[Clique 4]** Frase de transição: *"E se, em vez de uma árvore, usarmos centenas?"*

**Fala:** "Esse é um fenômeno conhecido: a média de muitas estimativas independentes costuma ser melhor do que quase qualquer estimativa individual, porque os erros para cima e para baixo se cancelam. Mas atenção à palavra 'independentes'. Se todas as árvores forem iguais, todas erram igual. Os próximos dois slides mostram como o Random Forest cria árvores diferentes."

### Slide 13 — Ingrediente 1: cada árvore estuda uma amostra diferente (Bootstrap)

- **[Inicial]** A tabela de treino completa
- **[Clique 1]** Árvore 1 recebe um sorteio *com reposição* de linhas; algumas pessoas aparecem repetidas e outras ficam de fora
- **[Clique 2]** Árvore 2 recebe outro sorteio; Árvore 3, outro...
- **[Clique 3]** Nota: *"Cerca de 37% das pessoas ficam de fora de cada árvore. Elas viram uma 'prova surpresa' gratuita: a validação out-of-bag."*

**Fala:** "Cada árvore treina com uma versão levemente diferente dos dados. Isso se chama bootstrap, e combinar árvores treinadas assim se chama bagging. E as pessoas que ficaram de fora de cada árvore servem para testar aquela árvore, sem gastar o conjunto de teste."

### Slide 14 — Ingrediente 2: cada pergunta vê só parte das variáveis

- **[Inicial]** Uma árvore prestes a fazer uma pergunta, com as 28 variáveis disponíveis
- **[Clique 1]** Um sorteio destaca só metade delas: *"Escolha a melhor pergunta usando apenas estas"*
- **[Clique 2]** Na próxima pergunta, um novo sorteio, com outras variáveis
- **[Clique 3]** Resultado: *"As árvores ficam diferentes entre si, então os erros delas também ficam diferentes."*

**Fala:** "É daqui que vem o 'Random' do nome. Sortear as variáveis impede que todas as árvores façam exatamente as mesmas perguntas. No nosso projeto, cada pergunta via 50% das variáveis."

### Slide 15 — A floresta: o consenso

- **[Inicial]** Uma pessoa nova entra pela esquerda
- **[Clique 1]** Ela passa por 300 árvores ao mesmo tempo; cada uma dá um palpite (5,2 / 6,1 / 5,7 / 4,9...)
- **[Clique 2]** **Previsão final = média dos 300 palpites = 5,6**
- **[Clique 3]** O gráfico completo aparece: árvore única 0,41 → árvore regularizada 0,61 → **Random Forest 0,71** em dados novos

**Visual:** `figures/02_arvore_vs_floresta.png` (completo, revelado no Clique 3).

**Fala:** "Esse é o Random Forest: muitas árvores diferentes, cada uma com seus erros, e o consenso entre elas. Com os mesmos dados, o desempenho em pessoas novas foi de 0,41 para 0,71."

### Slide 16 — Quantas árvores são suficientes?

- **[Inicial]** Gráfico do desempenho conforme o número de árvores
- **[Clique 1]** Destaque na subida rápida entre 30 e 100 árvores
- **[Clique 2]** Destaque no platô a partir de ~250: *"Mais árvores não pioram, só deixam de ajudar"*
- **[Clique 3]** Resumo dos hiperparâmetros: **300 árvores · 50% das variáveis por pergunta · mínimo de 10 pessoas por folha**

**Visual:** `figures/02_oob_vs_n_arvores.png` (avisar que o eixo vertical está ampliado).

**Fala:** "Uma propriedade bonita do Random Forest: adicionar árvores não causa overfitting, o resultado só estabiliza. Escolhemos 300, já no platô."

---

## Bloco 4 — O Projeto

### Slide 17 — A pergunta

- **[Inicial]** Em letras grandes: *"Redes sociais derrubam a nossa produtividade?"*
- **[Clique 1]** *"O senso comum diz que sim."*
- **[Clique 2]** *"Vamos perguntar aos dados, e deixar o Random Forest decidir o que importa."*

**Fala:** "Essa é a pergunta do nosso projeto. A gente tinha uma opinião formada, mas a proposta do Machine Learning é deixar os dados falarem."

### Slide 18 — O dataset

- **[Inicial]** Número grande: **30.000 pessoas**
- **[Clique 1]** **19 informações** sobre cada uma, agrupadas em cinco ícones: *Perfil · Hábitos digitais · Rotina de trabalho · Bem-estar · Ferramentas de foco*
- **[Clique 2]** Exemplos de hábitos: horas por dia em redes sociais, rede favorita (TikTok, Instagram, Facebook, Twitter, Telegram), notificações, tela antes de dormir
- **[Clique 3]** **Alvo:** produtividade real, de 0 a 10

**Fala:** "O dataset Social Media vs Productivity tem 30 mil pessoas, com hábitos digitais, rotina, bem-estar e a produtividade medida de cada uma."

### Slide 19 — O pipeline

- **[Inicial]** Seis caixas em sequência, ainda apagadas
- **[Clique 1]** **Exploração** (EDA) → **[Clique 2]** **Limpeza** (nulos, categorias em números) → **[Clique 3]** **Treino** (Random Forest) → **[Clique 4]** **Avaliação** (prova com dados novos) → **[Clique 5]** **Insights** (o que o modelo aprendeu) → **[Clique 6]** **Interface interativa**

**Visual:** versão simplificada do diagrama Mermaid do `README.md`.

**Fala:** "Esse foi o nosso caminho, e cada etapa está num notebook separado no repositório."

### Slide 20 — Primeira descoberta: a ilusão de produtividade

- **[Inicial]** Gráfico da produtividade percebida vs real
- **[Clique 1]** Destaque: **85% das pessoas se acham mais produtivas do que realmente são**, em média +0,56 ponto
- **[Clique 2]** Decisão técnica: *"Por isso NÃO usamos a produtividade percebida como entrada: seria prever a resposta usando a própria resposta (data leakage)."*

**Visual:** painel central e painel direito de `figures/01_produtividade_percebida_vs_real.png`.

**Fala:** "Antes de treinar qualquer coisa, a exploração já mostrou um comportamento humano interessante: a gente se superestima. E isso trouxe uma decisão importante: tiramos essa coluna do modelo, porque ela é praticamente a resposta disfarçada."

### Slide 21 — O modelo funciona?

- **[Inicial]** Gráfico de previsão vs realidade
- **[Clique 1]** Três números grandes: **R² = 0,72** · **erro médio = 0,78 ponto** · **72% das previsões a até 1 ponto do real**
- **[Clique 2]** Nota: *"Testado em 5.527 pessoas que o modelo nunca viu."*

**Visual:** painel esquerdo de `figures/03_previsto_vs_real.png`.

**Fala:** "O modelo explica cerca de 72% da variação da produtividade, em pessoas que ele nunca viu. Bem melhor do que chutar a média, que erraria 1,6 ponto. Mas a pergunta que interessa é: o que ele aprendeu?"

---

## Bloco 5 — Descobertas

### Slide 22 — O que o modelo usa para prever?

- **[Inicial]** Título: *"Se eu embaralhar esta informação, o modelo piora quanto?"*
- **[Clique 1]** A barra laranja aparece: **Satisfação com o trabalho**, gigante
- **[Clique 2]** As demais aparecem: todas praticamente **zero**
- **[Clique 3]** Frase: *"Entre 28 variáveis, o Random Forest encontrou sozinho a única que importa."*

**Visual:** painel esquerdo de `figures/04_feature_importance_permutacao.png`.

**Fala:** "Esse é o método de permutação: embaralhamos uma coluna e vemos quanto o modelo piora. Embaralhar a satisfação destrói o modelo. Embaralhar qualquer outra coisa, inclusive as redes sociais, não muda nada."

### Slide 23 — E as redes sociais?

- **[Inicial]** Pergunta: *"Se eu passar de 0 para 7 horas por dia nas redes sociais, minha produtividade prevista cai quanto?"*
- **[Clique 1]** O painel *Horas/dia em redes sociais* aparece: **uma linha reta**, com variação de 0,04 ponto
- **[Clique 2]** O painel *Satisfação com o trabalho* aparece ao lado: subida de **5,5 pontos**
- **[Clique 3]** Os outros painéis (notificações, tela antes de dormir, sono, estresse): **todos planos**

**Visual:** `figures/04_dependencia_parcial.png`, revelado painel a painel.

**Fala:** "Esse gráfico mostra como a previsão muda quando só uma variável muda. Redes sociais: reta. Notificações: reta. Sono: reta. A única curva que se mexe é a satisfação com o trabalho."

### Slide 24 — Simulação: "e se...?"

- **[Inicial]** Três cenários aplicados às 5.527 pessoas do teste
- **[Clique 1]** *E se todos usassem só 1 h/dia de redes, com poucas notificações?* → **0,00 ponto**
- **[Clique 2]** *E se todos usassem 8 h/dia, com muitas notificações?* → **−0,02 ponto**
- **[Clique 3]** *E se a satisfação de todos subisse 2 pontos?* → **+1,42 ponto**

**Visual:** `figures/04_simulacao_cenarios.png`.

**Fala:** "Pedimos ao modelo para imaginar mundos diferentes. Mudar radicalmente o uso de redes sociais não mexe na previsão. Mudar a satisfação mexe mais de um ponto. A rede favorita também não importa: a diferença entre TikTok e Facebook é de 0,02 ponto."

### Slide 25 — Plot twist: a Feature Importance pode mentir

- **[Inicial]** Pergunta: *"Mas a Feature Importance padrão do Random Forest dá ~1% para redes sociais. Isso não é um efeito pequeno?"*
- **[Clique 1]** Experimento: *"Adicionamos uma coluna de números sorteados ao acaso, sem relação com nada."*
- **[Clique 2]** O gráfico aparece: o **ruído aleatório fica em 2º lugar**, à frente das redes sociais
- **[Clique 3]** Lição: *"A importância padrão (MDI) premia até o ruído. Para concluir algo, use a permutação nos dados de teste."*

**Visual:** `figures/04_mdi_vs_ruido.png`.

**Fala:** "Esse foi o momento mais curioso do projeto. A importância que o Random Forest calcula por padrão colocou números aleatórios à frente das redes sociais. Ou seja, aquele 1% não era sinal, era o modelo se ajustando a ruído. É um cuidado que vale para qualquer projeto com Random Forest."

### Slide 26 — Um modelo simples empata

- **[Inicial]** Gráfico de comparação
- **[Clique 1]** Chute pela média: R² = 0
- **[Clique 2]** Regressão linear usando **só a satisfação**: R² = 0,713
- **[Clique 3]** Random Forest com 28 variáveis: R² = 0,716
- **[Clique 4]** Conclusão: *"Não havia padrões complexos escondidos. O sinal estava em uma única variável."*

**Visual:** painel esquerdo de `figures/03_comparacao_baselines.png`.

**Fala:** "Sempre comparem com um modelo simples. Aqui, uma regressão linear de uma variável quase empatou. Isso não é um fracasso do Random Forest: ele chegou ao melhor resultado possível com esses dados e ainda nos mostrou onde estava o sinal."

### Slide 27 — Cuidado ao generalizar

- **[Inicial]** Título: *"Então redes sociais não fazem mal?"*
- **[Clique 1]** **Dados sintéticos:** as variáveis não têm relação nenhuma entre si (nem sono com estresse), o que é improvável na vida real. O dataset parece gerado artificialmente.
- **[Clique 2]** **Correlação não é causalidade:** o modelo aprende associações, não causas.
- **[Clique 3]** **A pesquisa real é mais nuançada:** os efeitos negativos aparecem mais ligados a **interrupções** e ao **uso compulsivo** do que ao tempo total de tela.

**Fala:** "Precisamos ser honestos: o modelo aprendeu corretamente as regras deste dataset, mas este dataset não representa bem o mundo real. A conclusão 'redes sociais não importam' vale para estes dados, não para a vida de vocês."

### Slide 28 — O que aprendemos sobre Machine Learning

- **[Clique 1]** **1.** O modelo só aprende o que está nos dados. Dados sintéticos geram conclusões sintéticas.
- **[Clique 2]** **2.** Sempre compare com um baseline simples.
- **[Clique 3]** **3.** Desconfie da Feature Importance padrão; use permutação.
- **[Clique 4]** **4.** Um resultado "nulo" também é um resultado.

**Fala:** "Se fosse para levar só quatro coisas desta apresentação, seriam essas."

---

## Bloco 6 — Encerramento

### Slide 29 — Agora é com vocês: a interface interativa

- **[Inicial]** Título: *"Qual seria a SUA produtividade?"*
- **[Clique 1]** Captura de tela da interface Gradio: sliders de horas em redes sociais, notificações, sono e satisfação, além de menus para a rede favorita e a área de atuação
- **[Clique 2]** *"O modelo treinado roda em segundo plano e responde na hora."*
- **[Clique 3]** QR code ou link para o repositório no GitHub

**Visual:** captura de tela da interface da Fase 6 (`06_app.py`).

**Fala:** "Para fechar, o projeto conta com uma interface interativa. Qualquer pessoa ajusta os próprios hábitos e vê a previsão do modelo em tempo real. Vamos testar ao vivo."

**Roteiro da demonstração ao vivo (2 a 3 min):**

1. Começar com um perfil "médio" e mostrar a previsão.
2. Arrastar o slider de **redes sociais** de 1 h para 10 h: a previsão praticamente não muda. Retomar a descoberta do Slide 23.
3. Trocar a **rede favorita**: nada muda.
4. Arrastar o slider de **satisfação com o trabalho**: a previsão sobe ou desce vários pontos.
5. Pedir a um voluntário da turma que diga seus valores e mostrar a previsão.

### Slide 30 — Obrigado

- **[Inicial]** *"Obrigado! Perguntas?"*
- **[Inicial]** Link do repositório, nomes dos integrantes e frase final: *"Random Forest: muitas árvores diferentes, uma decisão melhor."*

---

## Apêndice A — Checklist de figuras

| Slide | Arquivo | Uso |
|---|---|---|
| 11, 15 | `figures/02_arvore_vs_floresta.png` | Recortar só a primeira linha no Slide 11 |
| 16 | `figures/02_oob_vs_n_arvores.png` | Avisar que o eixo está ampliado |
| 20 | `figures/01_produtividade_percebida_vs_real.png` | Painéis central e direito |
| 21 | `figures/03_previsto_vs_real.png` | Painel esquerdo |
| 22 | `figures/04_feature_importance_permutacao.png` | Painel esquerdo |
| 23 | `figures/04_dependencia_parcial.png` | Revelar painel a painel |
| 24 | `figures/04_simulacao_cenarios.png` | Completo |
| 25 | `figures/04_mdi_vs_ruido.png` | Completo |
| 26 | `figures/03_comparacao_baselines.png` | Painel esquerdo |
| 29 | Captura de tela da interface (Fase 6) | Gerar após a Fase 6 |

Figuras extras para perguntas da plateia: `01_redes_sociais_vs_produtividade.png`, `01_dose_resposta.png`, `01_matriz_correlacao.png`, `03_vies_por_faixa.png`, `04_importancia_por_tema.png`.

## Apêndice B — Perguntas prováveis da plateia

| Pergunta | Resposta curta |
|---|---|
| "Por que Random Forest e não uma rede neural?" | Em dados tabulares de tamanho médio, o Random Forest costuma ter desempenho competitivo, exige pouco ajuste, não precisa de normalização e é mais fácil de interpretar. |
| "Por que não usaram a produtividade percebida?" | Ela é uma autoavaliação da mesma coisa que queremos prever (correlação de 0,96). Usá-la seria vazamento de informação (Slide 20). |
| "O modelo erra em quem?" | Nos extremos: superestima quem é muito pouco produtivo e subestima quem é muito produtivo (~1 ponto), porque 28% da variação não é explicada por nenhuma variável (`03_vies_por_faixa.png`). |
| "Se o dataset é sintético, o projeto perdeu o valor?" | Não. O objetivo era aprender e aplicar o Random Forest. O projeto mostra o algoritmo encontrando o sinal, ignorando o ruído e sendo avaliado com rigor, e ainda ensina a questionar a qualidade dos dados. |
| "Por que 300 árvores?" | O desempenho estabiliza por volta de 250 (Slide 16); mais árvores só aumentam o custo. |

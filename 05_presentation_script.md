# Roteiro da Apresentação: Aprendizado de Máquina via Algoritmo Random Forest

**Disciplina:** Inteligência Artificial
**Estudo de caso:** Redes Sociais vs Produtividade
**Alunos:** Antônio Rodrigo Lima de Andrade Tenório (23210707) · Bruno Gomes de Barros Filho (21111360)
**Slides:** `05_slides.md` (39 slides, Marp) · **PDF:** `apresentacao.pdf`
**Duração:** cerca de 22 minutos de fala + 3 minutos de demonstração + perguntas

Este roteiro acompanha os slides **na mesma ordem e com a mesma numeração** do PDF. Cada slide traz quem fala, quanto tempo dura, o que aparece a cada clique e a fala sugerida.

---

## Como usar este roteiro

| Marcação | Significado |
|---|---|
| **Quem fala** | Antônio ou Bruno |
| **Tempo** | Tempo-alvo do slide |
| **Na tela** | O que aparece ao abrir o slide e a cada clique |
| **Fala** | Sugestão do que dizer. Não é para decorar palavra por palavra: é o raciocínio que precisa aparecer |
| **Transição** | Frase que liga ao próximo slide e evita o "próximo slide..." |
| **Atenção** | Pontos em que é fácil errar ou que o professor pode perguntar |

### Divisão entre os apresentadores

| Parte | Slides | Quem fala | Tempo |
|---|---|---|---|
| Abertura | 1 | Antônio | 0:30 |
| 1. Introdução à IA | 2 a 5 | Antônio | 2:30 |
| 2. Mergulho em Machine Learning | 6 a 10 | Antônio | 3:00 |
| 3. Random Forest, passo a passo | 11 a 22 | Bruno | 6:30 |
| 4. O Projeto | 23 a 28 | Antônio | 3:30 |
| 5. Descobertas | 29 a 36 | Bruno | 5:30 |
| 6. Demonstração e encerramento | 37 a 39 | Antônio (demo) e Bruno (fechamento) | 3:30 |

As trocas acontecem sempre nos slides azuis de seção, que funcionam como "passagem de bastão". Quem não está falando fica ao lado do computador e cuida dos cliques, se for o caso.

### Os cliques

- No **HTML exportado** (`apresentacao.html`), os tópicos com marcador aparecem **um por clique**. Imagens e tabelas aparecem junto com o slide.
- No **PDF** e na pré-visualização do VS Code, tudo aparece de uma vez. Se for apresentar pelo PDF, ignore as indicações de clique e siga a mesma ordem da fala.
- Tecla `P` no HTML abre o modo apresentador, com as notas de cada slide.

---

## Checklist antes da apresentação

**No dia anterior**

- [ ] Ensaiar com cronômetro pelo menos uma vez inteira, com a troca entre os dois.
- [ ] Gerar o HTML com cliques: `npx @marp-team/marp-cli 05_slides.md --allow-local-files -o apresentacao.html`.
- [ ] Copiar `apresentacao.pdf` e `apresentacao.html` para um pendrive e para o e-mail (plano B).
- [ ] Conferir que `models/random_forest.joblib` existe. A pasta `models/` não vai para o GitHub: em um computador novo, é preciso rodar antes os notebooks `01` e `02`.

**30 minutos antes**

- [ ] Abrir a interface: `uv run python 06_app.py` e deixar em uma aba do navegador em `http://127.0.0.1:7860`.
- [ ] Clicar uma vez em cada perfil pronto para "aquecer" o app.
- [ ] Abrir o `apresentacao.html` em tela cheia (`F11`), na primeira página.
- [ ] Testar o projetor: os gráficos têm texto pequeno, então confirmar que estão legíveis do fundo da sala.
- [ ] Desativar notificações do computador (seria irônico uma notificação aparecer no meio desta apresentação).

---

## Abertura

### Slide 1: Capa

**Quem fala:** Antônio · **Tempo:** 0:30

**Na tela:** título, subtítulo, disciplina e os nomes dos dois alunos.

**Fala:**
"Bom dia/boa tarde. Eu sou o Antônio, este é o Bruno, e o nosso tema é Aprendizado de Máquina via o algoritmo Random Forest. Para não ficar só na teoria, a gente aplicou o algoritmo numa pergunta que todo mundo aqui já se fez: será que o tempo nas redes sociais está acabando com a nossa produtividade? No final vocês vão poder testar o modelo ao vivo."

**Transição:** "Mas antes de chegar no Random Forest, precisamos dar um passo atrás: o que é, afinal, Inteligência Artificial?"

---

## Bloco 1: Introdução à Inteligência Artificial (Antônio)

### Slide 2: Seção "1. Introdução à Inteligência Artificial"

**Tempo:** 0:05. Só passar.

### Slide 3: O que é Inteligência Artificial?

**Tempo:** 0:50

**Na tela:**
- Clique 1: definição (tarefas que normalmente exigiriam inteligência humana)
- Clique 2: **Reconhecer**: rostos, voz, objetos
- Clique 3: **Entender**: textos e perguntas
- Clique 4: **Decidir**: rotas, recomendações
- Clique 5: **Prever**: clima, demanda, comportamento
- (o quadro com a frase sobre o feed aparece junto)

**Fala:**
"Inteligência Artificial é a área da computação que cria sistemas capazes de fazer tarefas que normalmente exigiriam inteligência humana. Não é só robô de filme. É reconhecer um rosto para desbloquear o celular, entender uma pergunta num assistente, decidir a melhor rota no GPS, prever o clima. E tem uma ironia: o feed da rede social de vocês, que é justamente o assunto do nosso projeto, é organizado por uma IA."

**Transição:** "E essa ideia é bem mais antiga do que parece."

### Slide 4: Uma linha do tempo rápida

**Tempo:** 0:50

**Na tela (um clique por marco):** 1950 Turing · 1956 Dartmouth · anos 1980–90 sistemas especialistas e ML · 2001 Random Forest · hoje.

**Fala:**
"Em 1950, Alan Turing já perguntava se as máquinas poderiam pensar. Em 1956, numa conferência em Dartmouth, o termo Inteligência Artificial foi criado. Nos anos 80 e 90 vieram os sistemas especialistas, em que alguém escrevia as regras à mão, e começou a crescer o Machine Learning. Em 2001, Leo Breiman publicou o Random Forest, que é o algoritmo de hoje. E hoje temos assistentes de IA, carros autônomos, diagnóstico por imagem. O que mudou de lá para cá foi a quantidade de dados e de poder de computação. E reparem: o Random Forest tem mais de 20 anos e continua sendo um dos algoritmos mais usados em dados de tabela."

**Atenção:** "dados tabulares" = dados em formato de planilha, com linhas e colunas.

### Slide 5: Onde entra o Machine Learning?

**Tempo:** 0:45

**Na tela:** diagrama de círculos: IA ⊃ Machine Learning ⊃ Deep Learning.

**Fala:**
"Machine Learning é uma parte da IA. A diferença é que, em vez de um programador escrever todas as regras, a máquina descobre as regras olhando exemplos. Dentro do Machine Learning está o Deep Learning, que usa redes neurais com muitas camadas. O Random Forest fica aqui, no Machine Learning clássico, e não é Deep Learning: não tem rede neural nenhuma, é feito de árvores de decisão."

**Transição:** "Então vamos entender melhor como uma máquina aprende com exemplos."

---

## Bloco 2: Mergulho em Machine Learning (Antônio)

### Slide 6: Seção "2. Mergulho em Machine Learning"

**Tempo:** 0:05

### Slide 7: Programar vs ensinar

**Tempo:** 0:50

**Na tela:** diagrama (Regras + Dados → Respostas, e Dados + Respostas → Regras).
- Clique 1: exemplo tradicional ("SE usa mais de 5 h de redes, ENTÃO é pouco produtivo")
- Clique 2: exemplo de ML ("Aqui estão 22 mil pessoas...")

**Fala:**
"Na programação tradicional, a gente dá as regras e os dados, e o computador devolve as respostas. Por exemplo: se a pessoa usa mais de 5 horas de rede social, então ela é pouco produtiva. Alguém inventou essa regra. No Machine Learning a gente inverte: entrega os dados e as respostas certas, e a máquina descobre as regras. É o que fizemos: entregamos 22 mil pessoas com a produtividade de cada uma e pedimos para o algoritmo descobrir o que importa. Guardem essa regra da esquerda, das 5 horas. No final vamos ver se ela sobrevive aos dados."

### Slide 8: Features e alvo

**Tempo:** 0:45

**Na tela:** tabela com 3 pessoas de exemplo.
- Cliques 1 a 3: Features · Alvo · O algoritmo procura padrões

**Fala:**
"Cada linha desta tabela é uma pessoa, ou seja, um exemplo. As colunas da esquerda, idade, horas de rede social, sono, satisfação, são as **features**: o que a gente sabe sobre a pessoa. A última coluna é o **alvo**: o que queremos prever, a produtividade. Com milhares de linhas, o algoritmo procura padrões que ligam as features ao alvo."

### Slide 9: Que tipo de pergunta estamos fazendo?

**Tempo:** 0:45

**Na tela:**
- Clique 1: Classificação (spam ou não)
- Clique 2: Regressão (produtividade de 0 a 10)
- Clique 3: Nosso caso: regressão

**Fala:**
"Isso é aprendizado **supervisionado**: a gente tem as respostas certas para o modelo aprender. Existem dois tipos principais de pergunta. Classificação, quando a resposta é uma categoria, como spam ou não spam. E regressão, quando a resposta é um número. A produtividade é uma nota com casas decimais, então o nosso problema é de regressão. A gente poderia dividir em baixa, média e alta, mas isso jogaria informação fora: uma pessoa com 4,9 e outra com 5,1 cairiam em classes diferentes, enquanto 3,4 e 4,9 ficariam na mesma."

**Atenção:** o Random Forest serve para os dois tipos. Usamos o `RandomForestRegressor` do scikit-learn.

### Slide 10: Treino e teste: a prova com questões inéditas

**Tempo:** 0:45

**Na tela:** barra 80% treino / 20% teste.
- Clique 1: o modelo é avaliado em pessoas que nunca viu
- Clique 2: Overfitting = decorar a matéria

**Fala:**
"Como saber se o modelo aprendeu de verdade? Do mesmo jeito que um professor: com uma prova de questões inéditas. Separamos 80% dos dados para o modelo estudar, o treino, e guardamos 20% que ele nunca vê, o teste. Se o modelo for ótimo no treino e ruim no teste, ele não aprendeu: ele **decorou**. Isso se chama **overfitting**, e é o aluno que tira 10 nos exercícios e vai mal na prova. Guardem esse nome, porque ele é o vilão do próximo bloco."

**Transição (passa para o Bruno):** "E é justamente para vencer esse vilão que existe o Random Forest. O Bruno vai mostrar como ele funciona."

---

## Bloco 3: Random Forest, passo a passo (Bruno)

> Este é o coração da apresentação. Falar devagar: cada slide acrescenta **uma** peça.

### Slide 11: Seção "3. Random Forest, passo a passo"

**Tempo:** 0:05

### Slides 12, 13 e 14: Peça 1: uma Árvore de Decisão

**Tempo:** 0:50 no total. Os três slides montam a mesma árvore aos poucos: avançar como se fossem cliques.

**Na tela:**
- Slide 12: só a pergunta "Satisfação com o trabalho > 5?"
- Slide 13: os galhos Sim e Não
- Slide 14: as folhas, com 3,8 (não) e 6,4 (sim)

**Fala:**
- (12) "A peça básica do Random Forest é a árvore de decisão. Ela funciona como um jogo de perguntas de sim ou não. Começa com uma pergunta..."
- (13) "...que divide as pessoas em dois grupos..."
- (14) "...e cada grupo recebe uma previsão, que é a média da produtividade das pessoas daquele grupo: 3,8 para quem tem satisfação até 5 e 6,4 para quem tem mais de 5. E esta árvore não é inventada: com os nossos dados, essa é exatamente a primeira pergunta que o algoritmo escolheu sozinho."

### Slide 15: A árvore cresce...

**Tempo:** 0:30

**Fala:**
"Em cada passo, o algoritmo testa todas as perguntas possíveis e escolhe a que mais reduz o erro. E se ninguém mandar parar, ele continua perguntando até cada folha ter uma única pessoa. No nosso treino foram 22.108 folhas: uma folha para cada pessoa."

**Transição:** "E uma folha para cada pessoa é um problema. Vejam o que acontece."

### Slide 16: Peça 2: o problema da árvore única

**Tempo:** 0:45

**Na tela (um clique por linha):** R² no treino 1,00 · R² em dados novos 0,41 · uma árvore sozinha decora e é instável.

**Fala:**
"O R² é a nota do modelo: 1 é acertar tudo, 0 é o mesmo que chutar a média. No treino, a árvore tirou 1,00: acertou 100% do que estudou. Em pessoas novas, 0,41. É o overfitting que o Antônio mostrou, acontecendo com os nossos dados. Cada folha aprendeu as particularidades de uma pessoa específica, e isso não se repete em gente nova. Além disso, a árvore é instável: mude poucas linhas dos dados e ela fica completamente diferente."

**Atenção:** explicar o R² aqui, porque ele volta nos slides 21, 22, 28 e 34.

### Slide 17: A ideia: sabedoria das multidões

**Tempo:** 0:45

**Na tela:** histograma de 400 chutes sobre a quantidade de balas num pote (valor real 500).
- Cliques 1 e 2: a média de centenas de chutes chega perto do real · e se usarmos centenas de árvores?

**Fala:**
"Imaginem um pote de balas com 500 balas. Um chute individual, como esse de 312, erra feio. Mas se 400 pessoas chutarem, uns erram para cima, outros para baixo, e a média fica muito perto de 500. Os erros se cancelam. Então a ideia é: e se, em vez de uma árvore, usarmos centenas? Só que tem um detalhe: isso só funciona se os chutes forem **diferentes** entre si. Se todas as árvores forem iguais, todas erram igual. Os próximos dois slides mostram como o Random Forest cria árvores diferentes."

### Slide 18: Ingrediente 1: cada árvore estuda uma amostra diferente

**Tempo:** 0:50

**Na tela:** diagrama de bootstrap (pessoas sorteadas para 3 árvores, algumas repetidas, outras de fora).
- Clique 1: Bootstrap, sorteio com reposição
- Clique 2: ~37% ficam de fora, a prova surpresa (out-of-bag)

**Fala:**
"Primeiro ingrediente: cada árvore estuda uma amostra diferente. A gente sorteia as pessoas **com reposição**: é como tirar um nome de um chapéu e devolver antes do próximo sorteio. Por isso algumas pessoas aparecem repetidas e outras ficam de fora. Isso se chama **bootstrap**, e combinar árvores treinadas assim se chama **bagging**. E tem um bônus: em média, uns 37% das pessoas ficam de fora de cada árvore. Elas viram uma prova surpresa gratuita para aquela árvore, chamada validação **out-of-bag**."

**Atenção:** se perguntarem "por que 37%?": a chance de uma pessoa nunca ser sorteada em n sorteios é (1 − 1/n)ⁿ, que tende a 1/e ≈ 0,37.

### Slide 19: Ingrediente 2: cada pergunta vê só parte das variáveis

**Tempo:** 0:40

**Na tela:** grade de variáveis com metade sorteada.
- Clique 1: em cada pergunta, novo sorteio (50% das variáveis)
- Clique 2: árvores diferentes erram de jeitos diferentes: é o "Random" do nome

**Fala:**
"Segundo ingrediente: em cada pergunta, a árvore não pode escolher entre todas as variáveis. Sorteamos só uma parte delas; no nosso projeto, metade. Na próxima pergunta, um novo sorteio. Isso impede que todas as árvores façam as mesmas perguntas, e é daqui que vem o 'Random' do nome."

### Slide 20: A floresta: o consenso

**Tempo:** 0:30

**Na tela:** uma pessoa nova passa por várias árvores (5,2 · 6,1 · 5,7 · 4,9 · 5,9...) → média = 5,6.

**Fala:**
"Juntando tudo: chega uma pessoa nova, ela passa pelas 300 árvores, cada árvore dá um palpite, e a previsão final é a média dos palpites. Isso é o Random Forest: muitas árvores diferentes, cada uma com os seus erros, e o consenso entre elas."

**Atenção:** em regressão é a **média**; em classificação seria a **votação** da maioria.

### Slide 21: Árvore única vs floresta

**Tempo:** 0:40

**Na tela:** gráfico comparando treino (azul) e dados novos (laranja) para árvore sem limite, árvore regularizada e Random Forest.

**Fala:**
"E funciona? Aqui está, com os nossos dados. Olhem as barras laranja, que são o desempenho em pessoas novas. A árvore sozinha: 0,41. Uma árvore com limites, para não decorar tanto, melhora. E a floresta chega a 0,71. Com os mesmos dados, só mudando o algoritmo."

### Slide 22: Quantas árvores são suficientes?

**Tempo:** 0:40

**Na tela:** curva do R² out-of-bag em função do número de árvores.
- Clique 1: sobe rápido até ~100 e estabiliza a partir de ~250
- Clique 2: escolhemos 300 árvores, 50% das variáveis, mínimo de 10 pessoas por folha

**Fala:**
"Quantas árvores colocar? Este gráfico mostra a nota out-of-bag conforme aumentamos as árvores. Atenção: o eixo vertical está ampliado, então a subida parece maior do que é. Sobe rápido até umas 100 e estabiliza depois de 250. Uma propriedade importante: mais árvores não causam overfitting, o resultado só para de melhorar. Escolhemos 300, já no platô. Também limitamos cada folha a ter no mínimo 10 pessoas, justamente para nenhuma árvore decorar uma pessoa só."

**Transição (passa para o Antônio):** "Agora que vocês sabem como o Random Forest funciona, o Antônio vai mostrar o que ele descobriu no nosso projeto."

---

## Bloco 4: O Projeto (Antônio)

### Slide 23: Seção "4. O Projeto"

**Tempo:** 0:05

### Slide 24: Redes sociais derrubam a nossa produtividade?

**Tempo:** 0:30

**Na tela:**
- Clique 1: o senso comum diz que sim
- Clique 2: vamos deixar o Random Forest decidir

**Fala:**
"A nossa pergunta. O senso comum diz que sim, e a gente também achava. Mas a proposta do Machine Learning é deixar os dados falarem. Então não dissemos ao modelo o que é importante: demos todas as informações e deixamos que ele descobrisse."

### Slide 25: O dataset

**Tempo:** 0:45

**Na tela (um clique por linha):** 30.000 pessoas e 19 informações · perfil · hábitos digitais · rotina e bem-estar · alvo.

**Fala:**
"Usamos o dataset Social Media vs Productivity, com 30 mil pessoas e 19 informações sobre cada uma. Perfil: idade, gênero, área de atuação. Hábitos digitais: horas em redes sociais, rede favorita, notificações por dia, tela antes de dormir. Rotina e bem-estar: horas de trabalho, pausas, café, sono, estresse, burnout e satisfação com o trabalho. E o alvo: a produtividade real, de 0 a 10."

### Slide 26: O pipeline

**Tempo:** 0:30

**Na tela:** as seis fases (exploração → limpeza → treino → avaliação → insights → interface).

**Fala:**
"Esse foi o nosso caminho, e cada fase é um notebook separado no repositório. Antes de treinar, tratamos os dados: removemos as cerca de 2.400 pessoas que não tinham a produtividade registrada, já que sem a resposta não dá para aprender, e preenchemos os demais valores vazios com a mediana. Também convertemos categorias como gênero e rede favorita em números, porque o modelo só entende números. Ficamos com 28 variáveis de entrada."

**Atenção:** a mediana foi escolhida porque os nulos são aleatórios (não dependem de nenhuma outra variável) e ela não é afetada por valores extremos. A conversão de categorias usou one-hot encoding.

### Slide 27: Primeira descoberta: a ilusão de produtividade

**Tempo:** 0:50

**Na tela:** gráfico da produtividade percebida vs real.
- Clique 1: 85% se acham mais produtivos do que são (+0,56 ponto)
- Clique 2: por isso não usamos a produtividade percebida (data leakage)

**Fala:**
"Antes mesmo de treinar, a exploração mostrou algo bem humano: o dataset também tem a produtividade que a pessoa **acha** que tem, e 85% das pessoas se acham mais produtivas do que realmente são, em média meio ponto a mais. E isso nos obrigou a tomar uma decisão importante: tiramos essa coluna do modelo. Ela tem correlação de 0,96 com a resposta. Usá-la seria como colar na prova: o modelo pareceria ótimo, mas estaria prevendo a resposta com a própria resposta. Isso se chama **vazamento de dados**, ou data leakage."

### Slide 28: O modelo funciona?

**Tempo:** 0:50

**Na tela:** gráfico de previsto vs real.
- Clique 1: R² = 0,72 · erro médio 0,78 ponto · 72% a até 1 ponto
- Clique 2: testado em 5.527 pessoas novas (chutar a média erraria 1,6 ponto)

**Fala:**
"E o modelo funciona? Na prova com 5.527 pessoas que ele nunca viu: R² de 0,72, ou seja, explica cerca de 72% da variação da produtividade. Erra em média 0,78 ponto numa escala de 0 a 10, e 72% das previsões ficam a até 1 ponto do valor real. Para comparar, chutar a média para todo mundo erraria 1,6 ponto. E a validação out-of-bag, que vimos antes, deu 0,71, praticamente o mesmo valor: sinal de que o resultado é estável. Mas a pergunta que realmente interessa é: **o que** ele aprendeu?"

**Transição (passa para o Bruno):** "E é aí que vem a parte mais surpreendente. O Bruno mostra."

---

## Bloco 5: Descobertas (Bruno)

### Slide 29: Seção "5. Descobertas"

**Tempo:** 0:05

### Slide 30: O que o modelo usa para prever?

**Tempo:** 0:50

**Na tela:** gráfico de importância por permutação (satisfação em laranja, enorme; o resto perto de zero; zoom à direita).
- Clique 1: "Se eu embaralhar esta informação, o modelo piora quanto?"
- Clique 2: entre 28 variáveis, encontrou sozinho a única que importa

**Fala:**
"Para descobrir o que o modelo usa, fizemos um teste simples: pegamos uma coluna, embaralhamos os valores dela entre as pessoas e medimos quanto o modelo piora. Se piorar muito, aquela informação era importante. Embaralhar a satisfação com o trabalho destrói o modelo. Embaralhar qualquer outra coisa, inclusive as horas de rede social, não muda praticamente nada. No painel da direita o eixo está ampliado umas 600 vezes, e mesmo assim tudo fica em volta de zero. Entre 28 variáveis, o Random Forest encontrou sozinho a única que importa."

### Slide 31: E as redes sociais?

**Tempo:** 0:45

**Na tela:** gráficos de dependência parcial (um por variável).
- Clique 1: de 0 a 7 h/dia de redes, a previsão muda 0,04 ponto; satisfação, 5,5 pontos

**Fala:**
"Este gráfico responde direto à nossa pergunta. Cada painel mostra como a previsão muda quando a gente varia **só** aquela variável e mantém o resto igual. Redes sociais: de 0 a 7 horas por dia, a previsão muda 0,04 ponto, uma reta. Notificações: reta. Sono e estresse: retas. A única curva que se mexe é a satisfação com o trabalho: 5,5 pontos de diferença."

### Slide 32: Simulação: "e se...?"

**Tempo:** 0:45

**Na tela (um clique por cenário):** só 1 h/dia → 0,00 · 8 h/dia com muitas notificações → −0,02 · satisfação +2 pontos → +1,42.

**Fala:**
"Também pedimos ao modelo para imaginar mundos diferentes, aplicando as mudanças nas 5.527 pessoas do teste. E se todo mundo usasse só 1 hora de rede social por dia? Zero de diferença. E se todo mundo usasse 8 horas, com muitas notificações? Menos 0,02 ponto. E se a satisfação de todos subisse 2 pontos? Mais 1,42 ponto. Até a rede favorita não importa: entre TikTok e Facebook, a diferença é de 0,02."

### Slide 33: Plot twist: a Feature Importance pode mentir

**Tempo:** 1:00. É o slide mais "técnico" e o que mais impressiona: não correr.

**Na tela:** gráfico da importância padrão (MDI) com uma coluna de ruído aleatório em 2º lugar.
- Clique 1: adicionamos uma coluna de números ao acaso, e ela ficou em 2º lugar
- Clique 2: a importância padrão (MDI) premia até ruído; use permutação nos dados de teste

**Fala:**
"Agora um plot twist. O Random Forest já calcula uma importância das variáveis por padrão, chamada MDI, e ela dava cerca de 1% de importância para as redes sociais. Parece pouco, mas não zero. Então fizemos um experimento: adicionamos uma coluna de números totalmente aleatórios, sem relação com nada. E essa coluna ficou em **segundo lugar**, na frente das redes sociais. Ou seja: aquele 1% não era sinal, era o modelo se ajustando a ruído. A importância padrão favorece variáveis com muitos valores diferentes, mesmo que sejam lixo. A lição: para tirar conclusões, usem a importância por permutação, medida nos dados de teste, que foi o que mostramos dois slides atrás."

### Slide 34: Um modelo simples empata

**Tempo:** 0:45

**Na tela:** comparação de R² entre chutar a média, regressão linear e Random Forest.
- Clique 1: regressão linear só com a satisfação, 0,713 · Random Forest, 0,716
- Clique 2: o sinal estava em uma única variável

**Fala:**
"Uma boa prática em Machine Learning é sempre comparar com um modelo simples. Uma regressão linear usando **só** a satisfação chegou a 0,713. O Random Forest com 28 variáveis, 0,716. Praticamente empate. Isso não é um fracasso do Random Forest: ele chegou ao melhor resultado possível com esses dados **e** nos mostrou onde estava o sinal. Simplesmente não havia padrões complexos escondidos."

**Atenção:** se perguntarem "então para que o Random Forest?": sem ele, não saberíamos que só a satisfação importava. Ele testou 28 variáveis, interações e relações não lineares, e confirmou que não havia mais nada.

### Slide 35: Então redes sociais não fazem mal?

**Tempo:** 0:50

**Na tela (um clique por tópico):** dados sintéticos · correlação não é causalidade · a pesquisa real é mais nuançada. O quadro "a conclusão vale para estes dados" aparece junto.

**Fala:**
"Então redes sociais não fazem mal? Calma. Precisamos ser honestos sobre três pontos. Primeiro: tudo indica que esse dataset é sintético, gerado artificialmente. As variáveis não têm relação nenhuma entre si, nem sono com estresse, o que seria muito improvável com pessoas reais. Segundo: correlação não é causalidade. O modelo aprende associações, não causas. Terceiro: a pesquisa real é mais complexa. Os efeitos negativos aparecem mais ligados a interrupções e uso compulsivo do que ao total de horas de tela. Então o modelo aprendeu corretamente as regras **deste** dataset, mas a conclusão vale para estes dados, não necessariamente para a vida de vocês."

**Atenção:** esse slide mostra senso crítico, e é um dos pontos que mais valorizam o trabalho. Falar com segurança, não como desculpa.

### Slide 36: O que aprendemos sobre Machine Learning

**Tempo:** 0:40

**Na tela (um clique por item):** 1) só aprende o que está nos dados · 2) compare com um baseline simples · 3) desconfie da Feature Importance padrão · 4) resultado nulo também é resultado.

**Fala:**
"Se fosse para levar só quatro coisas desta apresentação, seriam estas. Um: o modelo só aprende o que está nos dados; dados sintéticos geram conclusões sintéticas. Dois: sempre comparem com um modelo simples. Três: desconfiem da importância padrão e usem permutação. E quatro: um resultado 'nulo', como 'redes sociais não importam aqui', também é um resultado, e foi o Random Forest que nos permitiu afirmar isso com segurança."

**Transição (passa para o Antônio):** "Mas não precisam acreditar só na gente. Agora é com vocês."

---

## Bloco 6: Demonstração e encerramento

### Slide 37: Seção "6. Agora é com vocês"

**Quem fala:** Antônio · **Tempo:** 0:05

### Slide 38: Qual seria a SUA produtividade?

**Quem fala:** Antônio · **Tempo:** 0:30 de slide + 3:00 de demonstração

**Na tela:** captura da interface à direita.
- Cliques 1 a 4: interface Gradio · sliders e menus · resposta na hora com o palpite das 300 árvores · demonstração ao vivo

**Fala:**
"Fizemos uma interface com Gradio onde qualquer pessoa coloca os próprios hábitos e o modelo responde na hora. E ela mostra o palpite de cada uma das 300 árvores, ou seja, a floresta e o consenso que o Bruno explicou. Vamos testar."

**Roteiro da demonstração** (trocar para a aba do navegador com o app já aberto):

| Passo | Ação | O que deve aparecer | O que dizer |
|---|---|---|---|
| 1 | Clicar em **Perfil médio** | ~4,8 | "Uma pessoa típica: 3 h de redes, satisfação 5." Mostrar o histograma: "cada barrinha são árvores; a linha laranja é a média, a nossa previsão." |
| 2 | Aba **Hábitos digitais**: arrastar **redes sociais** de 1 h até 10 h | Muda menos de meio ponto (~4,8 → ~5,1) | "Dez horas por dia e a previsão quase não mexe. É o que vimos nos gráficos." |
| 3 | Trocar a **rede favorita** (TikTok, Facebook, Telegram) | Fica em ~4,85 a 4,9 | "A rede favorita também não importa." |
| 4 | Aba **Trabalho**: arrastar **satisfação** de 1 até 9 | ~2,2 → ~7,8 | "Agora a satisfação: mais de 5 pontos de diferença." |
| 5 | Clicar em **Muito conectado** e depois em **Muito satisfeito** | ~4,9 e ~7,8 | "Quem vive conectado fica na média. Quem está satisfeito vai lá em cima." |
| 6 (se houver tempo) | Pedir a um voluntário a satisfação e as horas de redes dele | | "Lembrando: vale para estes dados, não é diagnóstico!" |

**Atenção:** ao arrastar o slider de redes, a previsão pode subir um pouco, e não cair. Se alguém notar: "é variação aleatória das árvores, menor que o erro do próprio modelo, de 0,78 ponto."

**Plano B:** se o app não abrir, voltar ao slide 38 e descrever a captura de tela usando os números da tabela acima. Não tentar consertar ao vivo por mais de 30 segundos.

### Slide 39: Obrigado!

**Quem fala:** Bruno · **Tempo:** 0:15

**Fala:**
"Para fechar: Random Forest, muitas árvores diferentes, uma decisão melhor. Todo o código, os notebooks e a interface estão no repositório no GitHub. Obrigado, e ficamos à disposição para perguntas."

---

## Perguntas prováveis e respostas

Combinem antes: **perguntas sobre o algoritmo**, Bruno responde; **perguntas sobre dados, resultados e app**, Antônio responde. O outro complementa se precisar.

| Pergunta | Resposta curta |
|---|---|
| Por que Random Forest e não uma rede neural? | Em dados de tabela de tamanho médio, o Random Forest é competitivo, exige pouco ajuste, não precisa normalizar os dados e é mais fácil de interpretar. Rede neural brilha em imagem, texto e áudio. |
| Qual a diferença entre Random Forest e bagging? | Bagging só sorteia as linhas (bootstrap). O Random Forest sorteia as linhas **e** as variáveis em cada pergunta, o que deixa as árvores mais diferentes entre si. |
| Por que 300 árvores? | O desempenho estabiliza por volta de 250 (slide 22). Mais árvores não pioram, só aumentam o tempo. |
| Como escolheram os hiperparâmetros? | Comparamos algumas combinações pela nota out-of-bag, sem tocar no teste (notebook 02). O padrão `sqrt` sorteia só 5 das 28 variáveis e muitas perguntas ficavam sem acesso à satisfação; com 50% isso não acontece. `min_samples_leaf=10` impede que as folhas decorem pessoas individuais. |
| O que é o R²? | A proporção da variação do alvo que o modelo explica. 1 = perfeito, 0 = igual a chutar a média. |
| Por que tiraram a produtividade percebida? | Ela é uma autoavaliação da mesma coisa que queremos prever (correlação de 0,96). Usá-la seria vazamento de dados (slide 27). |
| Como trataram os valores vazios? | Removemos as linhas sem o alvo (não dá para aprender sem a resposta) e preenchemos as demais com a mediana, porque os nulos são aleatórios. |
| O modelo erra em quem? | Nos extremos: superestima quem é muito pouco produtivo e subestima quem é muito produtivo, porque 28% da variação não é explicada por nenhuma variável (`figures/03_vies_por_faixa.png`). |
| Se o dataset é sintético, o projeto perdeu o valor? | Não. O objetivo era aprender e aplicar o Random Forest. O projeto mostra o algoritmo encontrando o único sinal, ignorando o ruído e sendo avaliado com rigor, e ainda ensina a questionar a qualidade dos dados. |
| Por que não trocaram de dataset? | Porque o resultado honesto ensina mais: mostra baseline, armadilha da importância padrão e senso crítico com os dados. Trocar só porque o resultado não confirmou a nossa opinião seria viés de confirmação. |
| Uma regressão linear empatou. Então o Random Forest foi inútil? | Não: foi ele que testou as 28 variáveis, interações e relações não lineares e mostrou que só a satisfação importava. Sem isso, não saberíamos que o modelo simples bastava. |
| O que é out-of-bag? | As ~37% de pessoas que ficam fora do sorteio de cada árvore. Elas servem de teste para aquela árvore. Deu R² 0,71, igual ao teste (0,72). |
| O modelo tem overfitting? | Um pouco: R² 0,82 no treino e 0,72 no teste. É uma diferença pequena e esperada; a árvore única ia de 1,00 para 0,41. |

Figuras extras para responder perguntas (pasta `figures/`): `01_redes_sociais_vs_produtividade.png`, `01_dose_resposta.png`, `01_matriz_correlacao.png`, `03_residuos.png`, `03_vies_por_faixa.png`, `04_importancia_por_tema.png`.

---

## Se o tempo for curto (versão de 15 minutos)

Cortar sem perder a linha da história:

1. Slide 4 (linha do tempo): só citar 1956 e 2001.
2. Slides 8 e 9: juntar em uma fala de 30 segundos ("features são as entradas, o alvo é a produtividade, e como é um número, é regressão").
3. Slide 22: só dizer "usamos 300 árvores, onde o resultado já estabiliza".
4. Slide 32: citar apenas o cenário da satisfação (+1,42).
5. Demonstração: só os passos 1, 2 e 4.

**Nunca cortar:** slides 16 a 20 (como o Random Forest funciona), 27 (data leakage), 30 e 31 (a descoberta), 33 (o plot twist) e 35 (o senso crítico). São eles que mostram domínio do conteúdo.

## Dicas finais para a nota

- Olhar para a turma, não para a tela. Os gráficos são apoio, a explicação é de vocês.
- Sempre que mostrar um número, dizer o que ele significa ("0,78 ponto numa escala de 0 a 10").
- Usar as palavras técnicas e logo depois a tradução: "overfitting, ou seja, decorar".
- Ligar o começo ao fim: a regra das 5 horas do slide 7 é derrubada pelos slides 31 e 38. Vale lembrar isso em voz alta na demonstração.
- Se não souber uma resposta: "boa pergunta, não testamos isso, mas daria para verificar com..." é melhor do que inventar.

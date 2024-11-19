# 📺 YouTube Data Analysis: Insights from Science Channels

<p align="center">
  <a href="https://github.com/Edu-png">
    <img src="https://img.shields.io/badge/Autor-Eduardo%20Coqueiro-purple?style=flat&logo=github" alt="Autor">
  </a>
  <a href="mailto:eduardocoqueiro@gmail.com">
    <img src="https://img.shields.io/badge/Email-eduardocoqueiro%40gmail.com-purple?style=flat&logo=gmail" alt="Email">
  </a>
  <a href="https://linkedin.com/in/eduardocoqueiro/">
    <img src="https://img.shields.io/badge/LinkedIn-Eduardo%20Coqueiro-purple?style=flat&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://kaggle.com/EduardoCoqueiro">
    <img src="https://img.shields.io/badge/Kaggle-Eduardo%20Coqueiro-blue?style=flat&logo=kaggle" alt="Kaggle">
  </a>
</p>

![CAPAS - PROJETOS (6)](https://github.com/user-attachments/assets/5f0e1514-21ae-4fcb-92ed-3355f474aca5)

---
SUMA|RIO


## Resumo 📄

Este projeto foi desenvolvido para explorar métricas e estatísticas de canais do YouTube, com foco em canais de ciência e conteúdo educativo. Utilizando a **YouTube Data API** e técnicas de scraping, foram coletadas informações detalhadas sobre os canais e seus vídeos.

### Insights Obtidos:
- Canais internacionais tendem a ter mais visualizações devido à abrangência do idioma inglês.
- Canais brasileiros, apesar de parelhos em número de vídeos, possuem alcance mais limitado, destacando a importância do idioma para o público-alvo.
- Diferentes estratégias editoriais, como frequência de publicação e qualidade de produção, impactam significativamente as métricas de engajamento.

Este projeto fornece uma base para análise personalizada de canais no YouTube e pode ser adaptado para outros temas ou tipos de conteúdo.

## Introdução ☀

Com o crescimento exponencial de plataformas digitais como o YouTube, a análise de métricas de desempenho se tornou essencial para criadores de conteúdo e equipes de marketing. Este projeto utiliza a **YouTube Data API** para explorar estatísticas de canais científicos, destacando tendências e comportamentos no consumo de vídeos.

### Objetivo 🎯

1. **Explorar métricas de canais do YouTube:**
   - Extrair dados de inscritos, visualizações e total de vídeos de canais selecionados.
   - Identificar padrões no desempenho de vídeos.

2. **Fornecer insights estratégicos:**
   - Analisar quais fatores contribuem para maior engajamento e alcance.
   - Avaliar a frequência e impacto de publicações.

3. **Visualizar e interpretar dados:**
   - Criar gráficos que ajudem a entender tendências e comparações entre canais.
   - Destacar o impacto do idioma e da qualidade de produção no alcance de canais.

## Pipeline do Projeto 🛠

A execução deste projeto foi organizada em etapas bem definidas, garantindo uma análise estruturada e eficiente dos dados extraídos da **YouTube Data API**. Abaixo estão os passos detalhados:

---

### 1. **Configuração Inicial**
   - **Instalação de Bibliotecas:**
     - Instalação de dependências como `google-api-python-client` e `google-auth-oauthlib` para acessar a API do YouTube.
   - **Autenticação e Configuração:**
     - Configuração da API Key e criação de um serviço usando a documentação oficial da YouTube Data API.

---

### 2. **Extração de Dados de Canais**
   - **Identificação dos Canais:**
     - Seleção de canais científicos para análise, como "Kurzgesagt" e "Ciência Todo Dia".
   - **Extração de Métricas dos Canais:**
     - Utilização da API para coletar informações como:
       - Nome do canal.
       - Número de inscritos, visualizações e vídeos publicados.
       - ID da playlist de uploads.

---

### 3. **Transformação e Organização dos Dados**
   - **Construção de um DataFrame:**
     - Organização das métricas extraídas em um `DataFrame` com colunas: `Channel_name`, `Subscribers`, `Views`, `Total_videos`, entre outras.
   - **Conversão de Tipos de Dados:**
     - Transformação de colunas numéricas (como `Subscribers` e `Views`) para tipos apropriados.
   - **Cálculo de Métricas Adicionais:**
     - Adição de colunas derivadas para análises mais detalhadas.

---

### 4. **Análise Visual dos Dados dos Canais**
   - **Visualizações por Canal:**
     - Criação de gráficos para comparar:
       - Número de inscritos por canal.
       - Total de visualizações por canal.
       - Quantidade de vídeos publicados por canal.

---

### 5. **Extração de Dados Detalhados dos Vídeos**
   - **Obtenção de IDs de Vídeos:**
     - Coleta de todos os IDs de vídeos de cada canal utilizando as playlists de uploads.
   - **Coleta de Estatísticas dos Vídeos:**
     - Extração de detalhes como:
       - Título do vídeo.
       - Data de publicação.
       - Número de visualizações, curtidas e comentários.

---

### 6. **Análise de Métricas dos Vídeos**
   - **Exploração dos Dados:**
     - Organização das estatísticas dos vídeos em um `DataFrame`.
     - Conversão de tipos de dados para análise, como `views` e `likes`.
   - **Identificação de Destaques:**
     - Seleção dos 10 vídeos mais visualizados.
     - Cálculo de métricas agregadas, como vídeos por mês.

---

### 7. **Visualização dos Resultados**
   - **Gráficos de Desempenho:**
     - Gráficos destacando:
       - Vídeos mais visualizados.
       - Frequência de publicações por mês.
   - **Análises Contextuais:**
     - Observação de fatores que influenciam no desempenho, como idioma e qualidade de produção.

---

### 8. **Conclusões e Insights**
   - **Resumo dos Resultados:**
     - Identificação de padrões e fatores de sucesso entre os canais analisados.
   - **Possibilidades Futuras:**
     - Sugestões para criadores de conteúdo sobre frequência de postagens e estratégias para aumentar engajamento.

## Metodologia 🧪

A metodologia deste projeto foi dividida em etapas específicas para garantir a extração, organização, e análise eficiente dos dados dos canais e vídeos do YouTube. Abaixo, apresento cada etapa detalhadamente:

---

### 1. **Configuração e Autenticação**
- **Importação de Bibliotecas:**
  - Bibliotecas essenciais, como `google-api-python-client` e `pandas`, foram importadas para acessar a API do YouTube e manipular os dados.
- **Configuração da API:**
  - Foi gerada uma API Key no Google Cloud Console e utilizada para autenticação.
  - Criado um serviço com a função `build` da biblioteca `googleapiclient.discovery`.

---

### 2. **Extração de Dados dos Canais**
- **Seleção de Canais:**
  - Foi criada uma lista com os IDs dos canais de interesse, incluindo canais de ciência brasileiros e internacionais.
- **Coleta de Métricas:**
  - A função `youtube.channels().list` foi utilizada para obter:
    - Nome do canal.
    - Número de inscritos.
    - Total de visualizações.
    - Número de vídeos publicados.
    - ID da playlist de uploads (usado para acessar vídeos do canal).

---

### 3. **Transformação e Organização dos Dados**
- **Criação de DataFrame:**
  - Os dados extraídos foram organizados em um `DataFrame` para facilitar a análise e manipulação.
- **Conversão de Tipos de Dados:**
  - Colunas como `Subscribers` e `Views`, inicialmente armazenadas como strings, foram convertidas para tipos numéricos (`int`).

---

### 4. **Visualização Inicial dos Dados**
- **Gráficos por Canal:**
  - Foram gerados gráficos utilizando `seaborn` para visualizar:
    - Número de inscritos por canal.
    - Total de visualizações por canal.
    - Quantidade de vídeos publicados por canal.

---

### 5. **Extração de Dados dos Vídeos**
- **Coleta de IDs de Vídeos:**
  - Utilizando a ID da playlist de uploads, foi criada uma função para acessar todos os IDs de vídeos de cada canal.
- **Extração de Estatísticas dos Vídeos:**
  - A função `youtube.videos().list` foi usada para coletar informações detalhadas de cada vídeo, como:
    - Título do vídeo.
    - Data de publicação.
    - Número de visualizações, curtidas e comentários.

---

### 6. **Análise de Métricas dos Vídeos**
- **Organização dos Dados:**
  - As informações coletadas foram armazenadas em um `DataFrame` adicional, contendo detalhes de cada vídeo.
- **Conversão de Tipos e Transformações:**
  - Colunas como `views` e `likes` foram convertidas para tipos numéricos.
  - Foi adicionada uma coluna para identificar o mês de publicação de cada vídeo.
- **Seleção dos Destaques:**
  - Criada uma lista dos 10 vídeos mais visualizados para análises detalhadas.

---

### 7. **Visualização dos Resultados**
- **Gráficos de Métricas dos Vídeos:**
  - Foram criados gráficos para destacar:
    - Os 10 vídeos mais visualizados.
    - Frequência de publicações por mês.
- **Análise Contextual:**
  - Observações baseadas em padrões visuais, como o impacto da qualidade de produção e do idioma.

---

### Ferramentas Utilizadas
- **Google YouTube Data API:** Para extração de dados de canais e vídeos.
- **Pandas:** Para manipulação e organização dos dados em DataFrames.
- **Seaborn:** Para criação de gráficos e visualizações detalhadas.
- **Python:** Como linguagem principal para automação e análise.

Essa metodologia garantiu que os dados fossem coletados, tratados e analisados de forma eficiente, proporcionando insights relevantes sobre os canais e vídeos estudados.

## Resultados e Discussão 📊

### Resultados Obtidos

#### 1. **Estatísticas Gerais dos Canais**

A análise inicial revelou informações fundamentais sobre os canais selecionados. A tabela abaixo destaca as principais métricas coletadas:

| Canal                      | Inscritos   | Visualizações Totais | Total de Vídeos |
|----------------------------|-------------|-----------------------|-----------------|
| Kurzgesagt – In a Nutshell | 21.900.000  | 2.629.636.193         | 212             |
| CrashCourse                | 15.400.000  | 1.928.838.127         | 1.515           |
| Nerdologia                 | 3.350.000   | 404.659.178           | 995             |
| Ciência Todo Dia           | 4.760.000   | 774.307.879           | 913             |
| Atila Iamarino             | 1.620.000   | 102.382.351           | 314             |
| ColdFusion                 | 4.720.000   | 462.521.979           | 487             |
| Escaping Ordinary          | 1.210.000   | 43.500.728            | 15              |
| Universo Narrado           | 491.000     | 28.751.897            | 660             |

**Observações:**
- **Kurzgesagt – In a Nutshell** lidera em número de visualizações, mesmo com uma quantidade de vídeos significativamente menor que outros canais.
- **CrashCourse**, com mais de 1.500 vídeos, possui uma audiência robusta, destacando a importância de um grande volume de conteúdo.
- Os canais em português, como **Nerdologia** e **Ciência Todo Dia**, têm desempenho sólido em termos de inscritos e vídeos, mas apresentam menor alcance em visualizações devido ao público restrito pelo idioma.

---

#### 2. **Gráficos Gerados**

##### **Número de Inscritos por Canal**
![1](https://github.com/user-attachments/assets/6cf7fedd-f2eb-401e-adff-0fb303d956c3)


**Insights:**
- O idioma inglês amplia significativamente o alcance dos canais. **Kurzgesagt** e **CrashCourse** lideram com números expressivos de inscritos.
- Canais brasileiros, como **Nerdologia** e **Ciência Todo Dia**, possuem uma base de inscritos menor, embora sejam altamente reconhecidos no mercado nacional.

##### **Número de Visualizações por Canal**
![2](https://github.com/user-attachments/assets/b98ac0f8-51c4-4992-82dc-90d5fe924f30)


**Insights:**
- **Kurzgesagt – In a Nutshell** domina em visualizações, reforçando o impacto de conteúdo altamente editado e roteirizado.
- Apesar do grande número de vídeos, canais como **Atila Iamarino** e **Universo Narrado** possuem menor alcance, indicando que o volume de vídeos não é o único fator para engajamento.

##### **Número de Vídeos por Canal**
![3](https://github.com/user-attachments/assets/99b9a5df-4ecf-4586-a8b7-755289f3c664)

**Insights:**
- **CrashCourse** lidera em número de vídeos, mostrando uma estratégia baseada em volume.
- **Escaping Ordinary**, apesar de possuir apenas 15 vídeos, demonstra uma abordagem focada em conteúdo altamente específico e de nicho.

---

#### 3. **Top 10 Vídeos por Visualizações**

A tabela a seguir apresenta os vídeos mais populares entre os canais analisados, baseando-se no número de visualizações:

| Título                                          | Data Publicação | Visualizações  | Curtidas  | Comentários |
|------------------------------------------------|-----------------|----------------|-----------|-------------|
| Uma FOLHA dobrada 103 vezes fica MAIOR que o U | 2023-03-05      | 12.745.075     | 887.364   | 25.651      |
| Por que ISAAC NEWTON enfiou uma AGULHA no pró  | 2023-01-03      | 8.289.453      | 753.821   | 2.973       |
| Chernobyl: A História Completa                 | 2019-06-16      | 8.032.937      | 428.041   | 10.094      |

##### **Gráfico: Top 10 Vídeos**
![4](https://github.com/user-attachments/assets/6f7635d1-7ac8-41fa-ad52-40ce56364d07)


**Insights:**
- **Kurzgesagt** domina o ranking, com vídeos que combinam produção de alta qualidade e temas cientificamente intrigantes.
- Vídeos com títulos instigantes, como "Por que ISAAC NEWTON enfiou uma AGULHA no próprio olho?", atraem maior curiosidade e engajamento.

---

#### 4. **Quantidade de Vídeos Postados por Mês**

| Mês       | Quantidade |
|-----------|------------|
| Janeiro   | 71         |
| Fevereiro | 94         |
| Março     | 67         |

##### **Gráfico: Quantidade de Vídeos por Mês**
![5](https://github.com/user-attachments/assets/83161d03-b94d-4d3b-8faa-e7d118d0aff2)


**Insights:**
- Fevereiro apresenta o maior número de vídeos publicados, possivelmente relacionado a campanhas ou maior engajamento no início do ano.
- A análise mensal ajuda a identificar padrões de sazonalidade, sugerindo meses de maior atividade dos canais.

---

### Discussão

1. **Kurzgesagt – In a Nutshell como Referência de Sucesso:**
   - A abordagem de qualidade em vez de quantidade é claramente eficaz. Mesmo com um número limitado de vídeos, o canal domina em visualizações e engajamento.

2. **Impacto do Idioma:**
   - Canais em inglês possuem maior alcance global, como evidenciado por **Kurzgesagt** e **CrashCourse**. Já os canais em português são mais limitados em público-alvo, mas mantêm relevância regional.

3. **Produção versus Alcance:**
   - **Escaping Ordinary**, com apenas 15 vídeos, exemplifica como um nicho bem definido pode superar o volume em termos de impacto relativo.
   - A alta produção de canais como **CrashCourse** mostra que quantidade também pode ser uma estratégia eficaz quando aliada a uma base de público consolidada.

4. **Engajamento por Títulos e Temas:**
   - Títulos que provocam curiosidade científica, como "Chernobyl: A História Completa", têm um desempenho consistentemente alto.
   - Temas de ciência popular combinados com excelente qualidade de produção resultam em maior engajamento e compartilhamento.

Esses resultados destacam a importância de entender o público-alvo e alinhar a estratégia de produção com os objetivos de alcance e engajamento.

## Considerações Finais 🚀

Este projeto foi desenvolvido com o objetivo de explorar métricas de desempenho de canais científicos no YouTube, destacando tendências e características que podem orientar estratégias de conteúdo e engajamento. Durante a análise, foi possível identificar padrões importantes e tirar conclusões valiosas sobre os fatores que influenciam o sucesso de um canal.

---

### **Pontos de Destaque**

1. **Qualidade versus Quantidade:**
   - Canais como **Kurzgesagt – In a Nutshell** demonstram que a produção de vídeos altamente elaborados e roteirizados pode superar o impacto de um volume elevado de conteúdo.
   - Por outro lado, canais como **CrashCourse** mostram que consistência e volume também são estratégias eficazes para engajamento em longo prazo.

2. **Impacto do Idioma:**
   - Canais em inglês possuem maior potencial de alcance global, enquanto canais em português atendem a nichos regionais, mantendo relevância dentro do público falante da língua.

3. **Importância de Títulos e Temas:**
   - Títulos instigantes e temas de alta curiosidade científica atraem mais visualizações e interações, como curtidas e comentários.

4. **Padrões de Sazonalidade:**
   - A análise revelou meses de maior atividade, como fevereiro, que podem estar relacionados a campanhas específicas ou padrões sazonais de engajamento no YouTube.

---

### **Limitações**

1. **Acesso a Dados:**
   - Algumas limitações impostas pela API do YouTube restringem o volume de dados disponíveis, especialmente no que diz respeito a históricos mais extensos de vídeos.

2. **Foco Regional:**
   - A análise comparativa entre canais em inglês e português é limitada pela diferença natural de alcance global versus regional.

3. **Análises Não Quantitativas:**
   - Aspectos subjetivos, como qualidade de produção ou estratégia de marketing, não foram avaliados diretamente neste projeto.

---

### **Possibilidades de Expansão**

1. **Análise Detalhada de Tendências:**
   - Explorar a evolução do engajamento ao longo do tempo, identificando vídeos com maior crescimento contínuo.

2. **Estudo Comparativo Ampliado:**
   - Incluir mais canais e categorias além da ciência, para expandir o escopo da análise.

3. **Automatização e Monitoramento:**
   - Criar um pipeline para atualizar as métricas periodicamente, permitindo análises contínuas.

---

### **Conclusão**

Este projeto destacou a relevância de combinar dados quantitativos e qualitativos para entender o sucesso de canais no YouTube. Insights como a importância do idioma, a qualidade dos vídeos e padrões sazonais podem ajudar criadores de conteúdo a refinar suas estratégias. Com as melhorias sugeridas, esta análise pode se tornar uma ferramenta ainda mais robusta para decisões estratégicas no cenário digital.

## Agradecimentos 🙏

Gostaria de expressar minha profunda gratidão às seguintes pessoas e organizações que tornaram este projeto possível:

- **YouTube e Google Developers:**
  - Pela disponibilização da API do YouTube, que permitiu a extração e análise de métricas detalhadas dos canais.

- **Comunidade Científica e Criadores de Conteúdo:**
  - Aos canais analisados neste projeto, como **Kurzgesagt – In a Nutshell**, **Nerdologia**, e outros, por fornecerem conteúdo de qualidade e inspirarem a curiosidade científica em milhões de pessoas.

- **Mentores e Colegas:**
  - Por seu apoio durante o desenvolvimento deste projeto, fornecendo ideias, críticas construtivas e sugestões valiosas para melhorar a análise.

- **Ferramentas Open Source:**
  - Bibliotecas como `pandas`, `seaborn` e `google-api-python-client` foram fundamentais para a realização das análises e visualizações.

Este projeto foi realizado com o intuito de aprendizado e colaboração, refletindo o impacto positivo do compartilhamento de conhecimento e da curiosidade científica. Muito obrigado a todos os envolvidos direta ou indiretamente nesse processo!

<div align="center">
  <img src="https://github.com/user-attachments/assets/54afb33c-97be-40b6-8c96-0f12852e946f" alt="thank-you" width="500">
</div>

## 📞 Contato
- **LinkedIn:** [Eduardo Coqueiro](https://www.linkedin.com/in/eduardocoqueiro/)
- **Site:** [Eduardo Coqueiro](https://dataguy.my.canva.site/eduardo-coqueiro)
- **Kaggle:** [Eduardo Coqueiro](https://www.kaggle.com/eduardocoqueiro)


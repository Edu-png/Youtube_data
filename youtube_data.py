# -*- coding: utf-8 -*-
"""Youtube DATA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TqhQYpFYymVydluPcKUyal7mHJ_HoKnf

#**Atenção!**

*O Youtube agora bloqueia a obtenção do ID do usuário justamente pensando na privacidade dos dados, quando esse projeto foi realizado ainda era possível consultar. Deixei esse projeto disponível por ser focado em aprendizado e não haver intuito de prejudicar os responsáveis pelo canais, os quais eu admiro bastaste! Obrigado pela atenção!*
"""

# Rodando Local primeiramente é preciso instalar as bibliotecas para que possamos usar:

#pip install --upgrade google-api-python-client
#pip install --upgrade google-auth-oauthlib google-auth-httplib2 (Para autorização do usuário)


# Uma outra boa prática seria criar seu próprio ambiente para rodar esse projeto

###################################################################################################

# Importando as bibliotecas:

import pandas as pd
import seaborn as sns

# Importando módulos específicos:

from googleapiclient.discovery import build

# Criando as variáveis:

api_key = 'AIzaSyDMuYwOPLKHnelz360M21bBHRdFEToRWD0'
channel_id = 'UCsXVk37bltHxD1rDPwtNM8Q'

# Criando um service de acordo com a documentação do youtube (https://developers.google.com/youtube/v3/quickstart/python?hl=pt-br)
youtube = build('youtube', 'v3', developerKey = api_key)

# Extraindo os dados do canal por meio de uma função:

def get_channel_stats(youtube, channel_id):
  request = youtube.channels().list(
      part='snippet, contentDetails, statistics',
      id = channel_id)
  response = request.execute()

  return response

get_channel_stats(youtube, channel_id)
# Usando um formatador de JSON vamos obter esses dados de maneira mais amigável (https://jsonformatter.curiousconcept.com/#)

# Extraindo os dados do canal por meio de uma função de scrapper:

def get_channel_stats(youtube, channel_id):
  request = youtube.channels().list(
      part='snippet, contentDetails, statistics',
      id = channel_id)
  response = request.execute()

  data = dict(Channel_name = response['items'] [0] ['snippet']['title'], #vamos dar uma filtrada nas informações que vem criando um dicionário
              Subscribers = response['items'] [0] ['statistics']['subscriberCount'],
              Views = response['items'] [0] ['statistics']['viewCount'],
              Total_videos = response['items'] [0] ['statistics']['videoCount'])

  return data

# Podemos fazer isso para mais de um canal, então eu resolvi selecionar canais de ciência, dentre os quais alguns brasileiros:


# Criando as variáveis:

api_key = 'AIzaSyDMuYwOPLKHnelz360M21bBHRdFEToRWD0'
channel_ids = ['UCsXVk37bltHxD1rDPwtNM8Q', #Kurzgesagt – In a Nutshell
             'UClu474HMt895mVxZdlIHXEA', #Nerdologia
             'UC4QZ_LsYcvcq7qOsOhpAX4A', #ColdFusion
             'UCX6b17PVsYBQ0ip5gyeme-Q', #CrashCourse
             'UCSTlOTcyUmzvhQi6F8lFi5w', #Atila Iamarino
             'UCcf1t1tH-Pp5bmu4hbAytwA', #Escaping Ordinary
             'UCn9Erjy00mpnWeLnRqhsA1g', #Ciência todo dia
             'UCcdK7fNDtCuiERTzTZdWY7w'  #Universo Narrado
              ]

# Criando um service de acordo com a documentação do youtube (https://developers.google.com/youtube/v3/quickstart/python?hl=pt-br)
youtube = build('youtube', 'v3', developerKey = api_key)

# Extraindo os dados do canal por meio de uma função de scrapper:

def get_channels_stats(youtube, channels_ids):
  request = youtube.channels().list(
      part='snippet, contentDetails, statistics',
      id = ','.join(channel_ids)) #Como Channel_ids é uma lista, eu não posso passar aqui, então tenho que usar um método
  response = request.execute()

  return response

get_channels_stats(youtube, channel_ids)

# Novamente, vamos fazer isso de forma mais organizada, extraindo apenas as informações que desejamos

def get_channel_stats(youtube, channel_ids):
  all_data = [] #criando uma lista para fazer o loop
  request = youtube.channels().list(
      part='snippet, contentDetails, statistics',
      id = ','.join(channel_ids))
  response = request.execute()

# Agora como temos mais de um "item", uma abordagem que podemos seguir é fazer um loop para entrar em cada:

  for i in range(len(response['items'])):
    data = dict(Channel_name = response['items'] [i] ['snippet']['title'],
                Subscribers = response['items'] [i] ['statistics']['subscriberCount'],
                Views = response['items'] [i] ['statistics']['viewCount'],
                Total_videos = response['items'] [i] ['statistics']['videoCount'])
    all_data.append(data)

  return all_data

get_channel_stats(youtube, channel_ids)

# Usando pandas para colocar todos esses dados em um dataframe:

channel_statistics = get_channel_stats(youtube, channel_ids)

channel_data = pd.DataFrame(channel_statistics)

channel_data

# Aqui vemos que todas as colunas são objetos, e temos que trabalhar com valores numéricos
channel_data.dtypes

# Para isso, vamos fazer o processo de conversão de todos, menos do nome do canal:

channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])


channel_data.dtypes

# Vamos começar a plotar alguns resultados:

# Vendo o número de inscitos por canal:

# Número de views:

# Use uma paleta de cores diferente (por exemplo, 'viridis')
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channel_data, palette='Blues')

# Adicione rótulos e título
ax.set(xlabel='Nome do Canal', ylabel='Número de inscritos', title='Número de views por Canal')

# Gire os rótulos do eixo x para melhor legibilidade
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.show()

# Número de views:

# Use uma paleta de cores diferente (por exemplo, 'viridis')
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Channel_name', y='Views', data=channel_data, palette='Set3')

# Adicione rótulos e título
ax.set(xlabel='Nome do Canal', ylabel='Número de views', title='Número de views por Canal')

# Gire os rótulos do eixo x para melhor legibilidade
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.show()

# Número de vídeos:


# Use uma paleta de cores diferente (por exemplo, 'viridis')
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Channel_name', y='Total_videos', data=channel_data, palette='viridis')

# Adicione rótulos e título
ax.set(xlabel='Nome do Canal', ylabel='Número de Vídeos', title='Número de Vídeos por Canal')

# Gire os rótulos do eixo x para melhor legibilidade
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.show()

"""- Aqui ja podemos concluir coisas interessantes de maneira parcial, como por exemplo o fato de Kurzgesagt – In a Nutshell, ser um dos canais com menos vídeos e ainda assim o com mais vizualizações. Uma explicação para isso é que esse canal faz vídeos muito bem editados e roteirizados que demoram a sair.


- Vemos também que os canais brasileiros também perdem em views, mesmo estando parelhos em quantidade de vídeos, a explicação mais provável diz respeito ao idioma inglês ter uma abrangência muito maior que o português.


- No entanto, são necessárias analises mais detalahas para conclusões mais profundas.
"""

# Agora vamos trabalhar com todos os vídeos dos canais, fazendo o scrapper dos detalhes dos mesmos em suas playlists:

def get_channel_stats(youtube, channel_ids):
  all_data = []
  request = youtube.channels().list(
      part='snippet, contentDetails, statistics',
      id = ','.join(channel_ids))
  response = request.execute()

  for i in range(len(response['items'])):
    data = dict(Channel_name = response['items'] [i] ['snippet']['title'],
                Subscribers = response['items'] [i] ['statistics']['subscriberCount'],
                Views = response['items'] [i] ['statistics']['viewCount'],
                Total_videos = response['items'] [i] ['statistics']['videoCount'],
                playlist_id = response['items'] [i] ['contentDetails']['relatedPlaylists']['uploads'])
    all_data.append(data)

  return all_data

channel_statistics = get_channel_stats(youtube, channel_ids)

channel_data = pd.DataFrame(channel_statistics)

channel_data

# Entrando em playlist ID de um canal em particular
playlist_id = channel_data.loc[channel_data['Channel_name'] == 'Ciência Todo Dia', 'playlist_id'].iloc[0]
playlist_id

#Criando uma função para extrair os videos Ids de todos os canais.

def get_video_ids(youtube, playlist_id):

  request = youtube.playlistItems().list(
      part = 'contentDetails',
      playlistId = playlist_id,
      )
  response = request.execute()

  return response

get_video_ids(youtube, playlist_id)
# Por padrão a função retorna um resultado máximo de 5, mas podemos mudar isso caso necessário (maxResults)

#Mudando a função para resgatar mais resultados

def get_video_ids(youtube, playlist_id):

  request = youtube.playlistItems().list(
      part = 'contentDetails',
      playlistId = playlist_id
      )
  response = request.execute()

  video_ids = []

  for i in range(len(response['items'])):
    video_ids.append(response['items'][i]['contentDetails']['videoId'])

  next_page_token = response.get('nextPageToken')
  more_pages = True

  while more_pages:
    if next_page_token is None:
      more_pages = False
    else:
      request = youtube.playlistItems().list(
      part = 'contentDetails',
      playlistId = playlist_id,
      maxResults = 50,
      pageToken = next_page_token
      )
      response = request.execute ()

      for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

      next_page_token = response.get('nextPageToken')
  return video_ids

#Agora temos todas as 914 saidas de vídeo ids:
get_video_ids(youtube, playlist_id)

video_ids = get_video_ids(youtube, playlist_id)

video_ids

# Podemos criar uma função que resgate todos as informações desses vídeos agora:

def get_video_details(youtube, video_ids):
  all_video_stats = []

  for i in range(0, len(video_ids), 50):
    request = youtube.videos().list(
        part = 'snippet, statistics',
        id = ','.join(video_ids[i:i+50]))
    response = request.execute()

    for video in response ['items']:
      video_stats = dict(Title = video['snippet']['title'],
                         published_date = video['snippet']['publishedAt'],
                         views = video['statistics']['viewCount'],
                         likes = video['statistics']['likeCount'],
                         coments = video['statistics']['commentCount'])
      all_video_stats.append(video_stats)

  return all_video_stats

get_video_details(youtube, video_ids)

video_details = get_video_details(youtube, video_ids)

# Construindo o nosso data frame contendo as informações:
video_data = pd.DataFrame(video_details)

video_data

# Convertendo tudo para o formato correto:


video_data['published_date'] = pd.to_datetime(video_data['published_date']).dt.date
video_data['views'] = pd.to_numeric(video_data['views'])
video_data['likes'] = pd.to_numeric(video_data['likes'])

video_data

# Destacando algumas variáveis:

top10_videos = video_data.sort_values(by ='views', ascending = False).head(10)

top10_videos

# Vamos construir um gráfico trabalhando um pouco melhor nele:

# Configuração do tamanho da figura
sns.set(rc={'figure.figsize':(26,15)})

# Criação do gráfico de barras
ax1 = sns.barplot(x='views', y='Title', data=top10_videos, palette='husl')

# Ajusta o tamanho da fonte nos eixos x e y
ax1.set_xlabel('Views', fontsize=20)
ax1.set_ylabel('Title', fontsize=20)

# Ajusta o tamanho da fonte no eixo y
ax1.tick_params(axis='y', labelsize=15)

# Ajusta o tamanho da fonte no título do gráfico
ax1.set_title('Top 10 Videos', fontsize=25)

# Exibe o gráfico
plt.show()

# Vamos adicionar uma coluna de correspondência para o mês:
video_data['Month'] = pd.to_datetime(video_data['published_date']).dt.strftime('%b')

video_data

# Vendo quantos vídeos são postados por mês

videos_per_month = video_data.groupby('Month', as_index = False).size()
videos_per_month

# Colocando em ordem:

sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories = sort_order, ordered = True)

videos_per_month.sort_index()

# Vamos ver isso em formato de gráfico:

ax2 = sns.barplot(x = 'Month', y = 'size', data =videos_per_month, palette='Reds')

"""Então é isso, esse projeto permite analizar métricas de canais científicos escolhidos ou quaisquer outros que se deseje adicionar, muito obrigado por acompanhar meu trabalho nesse projeto que estou usando para estudar e qualquer sugestão por favor entre em contato."""
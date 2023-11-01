import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import plotly.express as px
import folium
#import numpy as np
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import branca.colormap

#from ..library import plot


# st.set_page_config(page_title="Analise dos dados do SEI", page_icon=":large_blue_square:", layout="wide")
st.header(':blue[Automação de Relatório de dados de Documentos]', divider='rainbow')
st.title("Litotecas onde teve mais Requisições")
st.caption("Projeto Final do Bootcamp de Análise de Dados - ENAP :game_die: :game_die: :game_die:")
st.caption("Turma Exclusiva para Mulheres - Outubro/2023 :cherry_blossom:")
# st.subheader('Análise dos dados do SEI :large_blue_square:', divider='rainbow')
#st.sidebar('auto')

# st.cache_data
# def gerar_df():
#     df = pd.read_excel('./data/rema.xlsx',
#                        engine='openpyxl')
#                        #usecols='I:W')
#                        #nrows=244)
#     return df

# df_excel = gerar_df()

# # df = pd.DataFrame(
# #      / [50, 50] + [37.76, -122.4],
# #     columns=['lat', 'lon'])

# st.map(df_excel)

litotecas_sgb = ['Litoteca Regional de Araraquara - LiAr', 'Litoteca Regional de Belém - Pará', 'Litoteca de Caçapava do Sul - Rio Grande do Sul',
                 'Litoteca Regional de Caeté - Minas Gerais', 'Litoteca Regional de Feira de Santana – Bahia', 'Litoteca Regional de Goiânia - Goiás',
                 'Litoteca Regional de Manaus - Amazônia', 'Litoteca Regional de Mossoró - Rio Grande do Norte', 'Litoteca Regional de Porto Velho - Rondõnia',
                 'Litoteca Regional de Teresina - Piauí']
litotecas_coordenadas = [[-21.794100, -48.174290],
                         [-1.454980, -48.502270],
                         [-30.515950, -53.483080],
                         [-19.885070, -43.662160],
                         [-12.2672, -38.9668],
                         [-16.6668, -49.25],
                         [3.117034, -60.025780],
                         [-5.2002, -37.3399],
                         [-8.74327, -63.91366],
                         [-5.08921, -42.8016]]

lats_longs = [[-21.794100, -48.174290, 4],
             [-1.454980, -48.502270, 10],
             [-30.515950, -53.483080, 16],
             [-19.885070, -43.662160, 14],
             [-12.2672, -38.9668, 1],
             [-16.6668, -49.25, 15],
             [3.117034, -60.025780, 8],
             [-5.2002, -37.3399, 3],
             [-8.74327, -63.91366, 5],
             [-5.08921, -42.8016, 0]
              ]

litotecas_mapa = folium.Map(location = [-17.8309, -58.0199], zoom_start=4, control_scale=True,
                            tiles ="cartodbpositron")
for i in range(len(litotecas_coordenadas)):

  coordenada = litotecas_coordenadas[i]
  litotecas = litotecas_sgb[i]
  folium.Marker(coordenada, popup=litotecas, icon = folium.Icon(icon = "câmera glyphicon", color = "green", icon_color="white",
               prefix = "glyphicon")).add_to(litotecas_mapa)

HeatMap(lats_longs).add_to(litotecas_mapa)
folium.LayerControl(position = "topleft").add_to(litotecas_mapa)

st_folium(litotecas_mapa, width=600)
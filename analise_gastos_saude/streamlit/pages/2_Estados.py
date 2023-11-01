import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Estados", page_icon="🏥", layout="wide")

st.title('_Análise Descritiva_ :hospital:')
st.markdown("---")


@st.cache_data
def gerar_df():
    df = pd.read_excel('./analise_gastos_saude/streamlit/data/variaveis_uf_ano.xlsx',
                       engine='openpyxl',
                       usecols='A:F',
                       nrows=244)
    return df


df = gerar_df()

nomes_originais = ['Gastos Hospitalares',
                   'Gastos Hosp. per capita', 'Mortalidade', 'Emendas Parlamentares']

anos = ['Escolha o ano', '2014', '2015', '2016',
        '2017', '2018', '2019', '2020', '2021', '2022']

estados = ['Escolha um estado', 'RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN',
           'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC',
           'RS', 'MS', 'MT', 'GO', 'DF']

with st.sidebar:
    st.sidebar.header("Nível de Agregação: UF")
    st.subheader('Seleção de Filtros')
    fvariavel = st.selectbox('Selecione a Variável:', options=nomes_originais)
    fano = st.selectbox('Selecione o Ano:', options=anos)
    fuf = st.selectbox('Selecione o Estado:', options=estados)

# filtrando a variável desejada
nomes_alvo = ['gastos', 'gastos_percapita', 'mortalidade', 'valor_emendas']
mapeamento = dict(zip(nomes_originais, nomes_alvo))
nome_alvo = mapeamento.get(fvariavel, fvariavel)
df_filtro = df[nome_alvo]

# filtrando ano
# filtrando ano
if fano != anos[0] and fuf != estados[0]:
    dados_usuario = df.loc[(df['ano'] == int(fano)) & (df['uf'] == fuf)]
elif fano != anos[0] and fuf == estados[0]:
    dados_usuario = df.loc[(df['ano'] == int(fano))]
elif fano == anos[0] and fuf != estados[0]:
    dados_usuario = df.loc[(df['uf'] == fuf)]
else:
    dados_usuario = df

col1, col2 = st.columns(2)


with col1:
    fig_barr_ano_uf = px.bar(dados_usuario.sort_values(by=nome_alvo, ascending=True), x='ano', y=nome_alvo, color='uf', template='plotly_dark').update_layout(
        barmode='relative', title=fvariavel, title_x=0.5).update_layout(
            legend_title_text='UF').update_xaxes(
                title='Ano', showgrid=False).update_yaxes(title=nome_alvo, showgrid=False)
    st.plotly_chart(fig_barr_ano_uf, theme=None, use_container_width=True)

with col2:
    fig_scatter_total = px.scatter(dados_usuario, x='ano', y=nome_alvo, title=fvariavel, template='plotly_dark').update_layout(
        title_x=0.5).update_xaxes(
            title='Ano', showgrid=False).update_yaxes(
                title=fvariavel, showgrid=False)
    st.plotly_chart(fig_scatter_total, theme=None, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    fig_barr_ano_uf_horizontal = px.bar(dados_usuario.sort_values(by=nome_alvo, ascending=True), x=nome_alvo, y='uf', color='ano', template='plotly_dark').update_layout(
        barmode='relative', title=fvariavel, title_x=0.5).update_layout(
            legend_title_text='Ano').update_xaxes(
                title=nome_alvo, showgrid=False).update_yaxes(
                    title='Estados', showgrid=False)
    st.plotly_chart(fig_barr_ano_uf_horizontal,
                    theme=None, use_container_width=True)

with col4:
    fig_barr_ano_uf = px.line(dados_usuario, x='ano', y=nome_alvo, color='uf', template='plotly_dark').update_layout(
        barmode='relative', title=fvariavel, title_x=0.5).update_layout(
            legend_title_text='UF').update_xaxes(
                title='Ano', showgrid=False).update_yaxes(title=nome_alvo, showgrid=False)
    st.plotly_chart(fig_barr_ano_uf, theme=None, use_container_width=True)


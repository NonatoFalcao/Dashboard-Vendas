import streamlit as st
import plotly.io as pio
from pathlib import Path

st.set_page_config(page_title="Dashboard de Vendas de Jogos", layout="wide")
st.title("Dashboard de Vendas de Jogos")

# Pasta onde estão os JSONs
fig_path = Path("Figuras")

# --- Seção 1: Vendas Globais por Ano ---
st.header("Evolução das Vendas Globais por Ano")
fig_vendas_ano = pio.read_json(fig_path / "fig_VendasAno.json")
st.plotly_chart(fig_vendas_ano, use_container_width=True)

# --- Seção 2: Gêneros por continente ---
st.header("Gêneros mais comprados por continente")
continente = st.selectbox("Escolha o continente:", ["EU","NA","JP","Others"])
fig_map = {
    "EU": "fig_GenEU.json",
    "NA": "fig_GenNA.json",
    "JP": "fig_GenJP.json",
    "Others": "fig_GenOthers.json"
}
fig_gen = pio.read_json(fig_path / fig_map[continente])
st.plotly_chart(fig_gen, use_container_width=True)

# --- Seção 3: Plataformas ---
st.header("Plataformas mais vendidas")
periodo = st.selectbox("Escolha o período:", ["Antes dos Anos 2000", "Depois dos Anos 2000"])
fig_map_plat = {
    "Antes dos Anos 2000": "fig_PlatMillennial.json",
    "Depois dos Anos 2000": "fig_PlatZ.json"
}
fig_plat = pio.read_json(fig_path / fig_map_plat[periodo])
st.plotly_chart(fig_plat, use_container_width=True)

# --- Seção 4: Relação Continente x Global ---
st.header("Relação Vendas Continente x Global")
continente_scatter = st.selectbox("Escolha o continente:", ["NA","EU","JP","Others"])
fig_map_scatter = {
    "NA": "fig_RelacaoNA.json",
    "EU": "fig_RelacaoEU.json",
    "JP": "fig_RelacaoJP.json",
    "Others": "fig_RelacaoOther.json"
}
fig_scatter = pio.read_json(fig_path / fig_map_scatter[continente_scatter])
st.plotly_chart(fig_scatter, use_container_width=True)


import os
charts_folder = "Figuras"

# Dicionário para armazenar os gráficos filtrados
charts_json = {}

# Carrega apenas arquivos que começam com "fig_EvoGen" e terminam com ".json"
for file in os.listdir(charts_folder):
    if file.startswith("fig_EvoGen") and file.endswith(".json"):
        # Pega o nome do gênero
        genre = file.replace("fig_EvoGen", "").replace(".json", "")
        # Abre o arquivo e converte de JSON para gráfico Plotly
        with open(os.path.join(charts_folder, file), "r") as f:
            charts_json[genre] = pio.from_json(f.read())

# Lista de gêneros para o slider
genres_list = list(charts_json.keys())

# Slider para escolher o índice do gênero
index = st.slider("Escolha o gráfico pelo índice", 0, len(genres_list)-1, 0)

# Mostra o gráfico correspondente
selected_genre = genres_list[index]
st.write(f"**Gênero:** {selected_genre}")
st.plotly_chart(charts_json[selected_genre])
import streamlit as st
import plotly.io as pio
from pathlib import Path
import os

# Configuração da página
st.set_page_config(page_title="🎮 Dashboard de Vendas de Jogos", layout="wide")
st.title("🎮 Dashboard de Vendas de Jogos")

fig_path = Path("Figuras")

# --- Seção 1: Vendas Globais por Ano ---
st.header("📈 Evolução das Vendas Globais por Ano")
fig_vendas_ano = pio.read_json(fig_path / "fig_VendasAno.json")
st.plotly_chart(fig_vendas_ano, use_container_width=True)

st.markdown("---")  # separador visual

# --- Seção 2: Gêneros por continente ---
st.header("🌍 Gêneros mais comprados por continente")
continente = st.selectbox("Escolha o continente 🌎:", ["EU","NA","JP","Others"])
fig_map = {
    "EU": "fig_GenEU.json",
    "NA": "fig_GenNA.json",
    "JP": "fig_GenJP.json",
    "Others": "fig_GenOthers.json"
}
fig_gen = pio.read_json(fig_path / fig_map[continente])
st.plotly_chart(fig_gen, use_container_width=True)

st.markdown("---")

# --- Seção 3: Plataformas ---
st.header("🕹️ Plataformas mais vendidas")
periodo = st.selectbox("Escolha o período ⏳:", ["Antes dos Anos 2000", "Depois dos Anos 2000"])
fig_map_plat = {
    "Antes dos Anos 2000": "fig_PlatMillennial.json",
    "Depois dos Anos 2000": "fig_PlatZ.json"
}
fig_plat = pio.read_json(fig_path / fig_map_plat[periodo])
st.plotly_chart(fig_plat, use_container_width=True)

st.markdown("---")

# --- Seção 4: Relação Continente x Global ---
st.header("📊 Relação Vendas Continente x Global")
continente_scatter = st.selectbox("Escolha o continente 🗺️:", ["NA","EU","JP","Others"])
fig_map_scatter = {
    "NA": "fig_RelacaoNA.json",
    "EU": "fig_RelacaoEU.json",
    "JP": "fig_RelacaoJP.json",
    "Others": "fig_RelacaoOther.json"
}
fig_scatter = pio.read_json(fig_path / fig_map_scatter[continente_scatter])
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# --- Seção 5: Evolução de Vendas por Gênero ---
st.header("🎨 Evolução de Vendas por Gênero")
charts_folder = "Figuras"
charts_json = {}

for file in os.listdir(charts_folder):
    if file.startswith("fig_EvoGen") and file.endswith(".json"):
        genre = file.replace("fig_EvoGen", "").replace(".json", "")
        with open(os.path.join(charts_folder, file), "r") as f:
            charts_json[genre] = pio.from_json(f.read())

genres_list = list(charts_json.keys())

# Slider com emojis de seta para indicar seleção
index = st.slider("Escolha o gráfico pelo índice ⬅️➡️", 0, len(genres_list)-1, 0)

selected_genre = genres_list[index]
st.subheader(f"🎯 Gênero selecionado: {selected_genre}")
st.plotly_chart(charts_json[selected_genre], use_container_width=True)

st.markdown("---")

# --- Seção 6: Plataformas Mais Compradas por Continente ---

st.header("🌍 Plataformas Mais Compradas por Continente")
continente = st.selectbox("Escolha o continente 🌎:", ["EU","NA","JP","Others", "Global"])
fig_map2 = {
    "EU": "fig_platEU.json",
    "NA": "fig_platNA.json",
    "JP": "fig_platJP.json",
    "Others": "fig_platOther.json",
    "Global": "fig_platGlobal.json"
}
fig_gen2 = pio.read_json(fig_path / fig_map2[continente])
st.plotly_chart(fig_gen2, use_container_width=True)

st.markdown("---")

# --- Seção 7: Jogos Mais Vendidos em Cada Decada ---

st.header("📊 Jogos Mais Vendidos em Cada Decada")
fig_vendas_decada = pio.read_json(fig_path / "fig_Games.json")
st.plotly_chart(fig_vendas_decada, use_container_width=True)

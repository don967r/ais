import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import plotly.express as px
from streamlit_folium import st_folium
from datetime import timedelta

# Инициализация состояния сессии
if 'spills_data' not in st.session_state:
    st.session_state.spills_data = None
if 'ais_data' not in st.session_state:
    st.session_state.ais_data = None
if 'time_window' not in st.session_state:
    st.session_state.time_window = 24

# --- 1. Конфигурация страницы и Заголовок ---
st.set_page_config(layout="wide", page_title="Анализ 'Судно-Пятно'")

st.title("🚢 Анализ связи 'Судно-Пятно' 💧")
st.write("""
Загрузите GeoJSON с полигонами разливов и CSV-файл с данными AIS.
Приложение автоматически найдет суда, которые находились в зоне разлива незадолго до его обнаружения,
и предоставит расширенную аналитику по инцидентам.
""")

# --- 2. Боковая панель с загрузчиками и параметрами ---
st.sidebar.header("Параметры анализа")

spills_file = st.sidebar.file_uploader(
    "1. Загрузите GeoJSON с полигонами разливов",
    type=["geojson", "json"],
    key="spills_uploader"
)

ais_file = st.sidebar.file_uploader(
    "2. Загрузите CSV с данными AIS",
    type=["csv"],
    key="ais_uploader"
)

# Используем сохраненное значение по умолчанию
time_window_hours = st.sidebar.slider(
    "3. Временное окно поиска (часы до обнаружения):",
    min_value=1, max_value=168, 
    value=st.session_state.time_window,  # Используем сохраненное значение
    step=1,
    help="Искать суда, которые были в зоне разлива за указанное количество часов ДО его обнаружения."
)

# Обновляем состояние при изменении
st.session_state.time_window = time_window_hours

# --- 3. Функции для обработки и анализа данных ---

@st.cache_data
def load_spills_data(uploaded_file):
    # ... (остается без изменений, как в оригинальном коде) ...

@st.cache_data
def load_ais_data(uploaded_file):
    # ... (остается без изменений, как в оригинальном коде) ...

def find_candidates(spills_gdf, vessels_gdf, time_window_hours):
    # ... (остается без изменений, как в оригинальном коде) ...

# --- 4. Основная логика приложения ---
def main():
    # Обработка загрузки файлов
    if spills_file:
        st.session_state.spills_data = load_spills_data(spills_file)
    if ais_file:
        st.session_state.ais_data = load_ais_data(ais_file)

    spills_gdf = st.session_state.spills_data
    vessels_gdf = st.session_state.ais_data

    if spills_gdf is not None and vessels_gdf is not None:
        # Проверка на пустые данные
        if spills_gdf.empty or vessels_gdf.empty:
            st.error("Один из датасетов пуст после обработки!")
            return

        candidates_df = find_candidates(spills_gdf, vessels_gdf, time_window_hours)

        # ... (остальная часть визуализации и аналитики без изменений) ...
        # Полный код визуализации из оригинального приложения
        # ...
    elif spills_gdf is not None or vessels_gdf is not None:
        st.info("Загрузите оба файла для анализа")
    else:
        st.info("⬅️ Пожалуйста, загрузите оба файла на боковой панели, чтобы начать анализ.")

# Запускаем основное приложение
if __name__ == '__main__':
    main()

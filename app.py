import streamlit as st
import introduction
import basics
import applications
import advanced
from PIL import Image
import auth
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from user_data import UserData
import streamlit.components.v1 as components
import pickle
from pathlib import Path
from user_cabinet import show_cabinet
import pandas as pd
import plotly.express as px
import streamlit_pandas_profiling as st_profile

# Создаем экземпляр класса UserData
user_data = UserData()

# Загружаем данные пользователей из файла
try:
    with open('user_data.pkl', 'rb') as f:
        user_data.users = pickle.load(f)
except FileNotFoundError:
    pass

# Настройка страницы
st.set_page_config(
    page_title="Python для аграриев",
    page_icon=":seedling:",
    layout="wide"
)

# Загрузка CSS-стилей
with open("styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Функция для загрузки анимированного изображения
@st.cache_data()
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Функция для отображения панели авторизации и кабинета
def show_auth_panel():
    auth_panel = st.container()
    with auth_panel:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Авторизация", key="auth_button"):
                username = st.text_input("Имя пользователя")
                password = st.text_input("Пароль", type="password")
                if user_data.authenticate_user(username, password):
                    st.success(f"Добро пожаловать, {username}!")
                    st.session_state["username"] = username
                else:
                    st.error("Неверный пароль. Доступ запрещен.")
        with col2:
            if st.button("Кабинет", key="cabinet_button"):
                show_cabinet(st.session_state.get("username", None), user_data)

# Функция для отображения главной страницы
def show_home():
    container = st.container()
    with container:
        col1, col2 = st.columns([1, 2])
        with col1:
            lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
            if lottie_coding:
                st_lottie(lottie_coding, height=300, key="lottie_animation")
            else:
                st.warning("Не удалось загрузить анимированное изображение.")
        with col2:
            st.markdown("<h2>Добро пожаловать в обучающее пособие по Python для аграриев!</h2>", unsafe_allow_html=True)
            st.markdown("<p>Это пособие предназначено для изучения основ программирования на Python и его применения в аграрной сфере.</p>", unsafe_allow_html=True)
            st.markdown("<p>Выберите раздел в боковом меню, чтобы начать обучение.</p>", unsafe_allow_html=True)
            
            # Интерактивный график
            data = pd.DataFrame({
                'Year': [2018, 2019, 2020, 2021, 2022],
                'Yield': [2.4, 2.9, 3.2, 3.8, 4.0]
            })
            fig = px.line(data, x='Year', y='Yield', title='Урожайность за последние 5 лет')
            st.plotly_chart(fig)

            # PDF загрузка
            pdf_file = st.file_uploader("Загрузите PDF-файл с дополнительными материалами", type=["pdf"])
            if pdf_file is not None:
                with open(f"{pdf_file.name}", "wb") as f:
                    f.write(pdf_file.getbuffer())
                st.success(f"Файл '{pdf_file.name}' успешно загружен.")
                
    st.image("https://cdn.pixabay.com/photo/2017/03/23/20/27/farmer-2169637_960_720.jpg", use_column_width=True)

# Главное меню
def main_menu():
    with st.sidebar:
        st.markdown("# Оглавление")
        menu = ["Главная", "Введение", "Основы программирования", "Применение в аграрных задачах", "Дополнительные темы", "Экзамены"]
        choice = option_menu(
            menu_title=None,
            options=menu,
            icons=["house", "book", "code", "tractor", "gear", "clipboard-check"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            styles={
                "container": {"padding": "0!important"},
                "icon": {"color": "orange", "font-size": "18px"},
                "nav-link": {
                    "font-family": "Arial",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee"
                },
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
        if choice == "Введение":
            st.markdown("### Введение")
            if st.sidebar.button("Что такое Python"):
                introduction.show_chapter1()
            if st.sidebar.button("Зачем нужен Python"):
                introduction.show_chapter2()
            if st.sidebar.button("Установка Python"):
                introduction.show_chapter3()
        elif choice == "Основы программирования":
            st.markdown("### Основы программирования")
            if st.sidebar.button("Переменные и типы данных"):
                basics.show_data_types()
            if st.sidebar.button("Условные операторы"):
                basics.show_control_structures()
            if st.sidebar.button("Циклы"):
                basics.show_loops()
            if st.sidebar.button("Функции"):
                basics.show_functions()
    return choice

# Основной контент
def main():
    show_auth_panel()
    choice = main_menu()
    if choice == "Главная":
        show_home()
    elif choice == "Введение":
        introduction.show_content()
        if st.button("Перейти к тесту"):
            introduction.show_test("Введение")
    elif choice == "Основы программирования":
        basics.show()
        show_test("Основы программирования")
    elif choice == "Применение в аграрных задачах":
        applications.show()
        show_test("Применение в аграрных задачах")
    elif choice == "Дополнительные темы":
        advanced.show()
        show_test("Дополнительные темы")
    elif choice == "Экзамены":
        show_exams()

def show_test(chapter):
    st.subheader(f"Тест по разделу '{chapter}'")
    # Добавьте здесь код для отображения теста

def show_exams():
    st.title("Экзамены")
    exams = ["Экзамен по введению", "Экзамен по основам программирования", "Экзамен по применению в аграрных задачах", "Экзамен по дополнительным темам"]
    selected_exam = st.selectbox("Выберите экзамен", exams)
    if selected_exam == "Экзамен по введению":
        introduction.show_exam()
    elif selected_exam == "Экзамен по основам программирования":
        basics.show_exam()
    elif selected_exam == "Экзамен по применению в аграрных задачах":
        applications.show_exam()
    elif selected_exam == "Экзамен по дополнительным темам":
        advanced.show_exam()

with open("scripts.js") as f:
    components.html(f"<script>{f.read()}</script>", height=200)

def save_user_data():
    with open('user_data.pkl', 'wb') as f:
        pickle.dump(user_data.users, f)

if __name__ == "__main__":
    main()
    save_user_data()

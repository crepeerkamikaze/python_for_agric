import streamlit as st
from streamlit_lottie import st_lottie_spinner
from streamlit_player import st_player
import requests

# Функция для загрузки анимированного изображения
@st.cache_data()
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_content():
    # Добавляем CSS-стили
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Создаем контейнер для навигации по разделам и подразделам
    navigation_container = st.container()

    # Контейнер с навигацией
    with navigation_container:
        sections = ["Что такое Python", "Зачем нужен Python", "Установка Python", "Дополнительная тема 1", "Дополнительная тема 2"]
        selected_section = st.selectbox("Выберите раздел", sections)
        show_introduction(selected_section)

def show_introduction(section):
    if section == "Что такое Python":
        show_chapter1()
    elif section == "Зачем нужен Python":
        show_chapter2()
    elif section == "Установка Python":
        show_chapter3()
    elif section == "Дополнительная тема 1":
        show_chapter4()
    elif section == "Дополнительная тема 2":
        show_chapter5()

def show_chapter1():
    st.header("Что такое Python?")
    with open("data/introduction/chapter1.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

    # Загружаем анимированное изображение
    lottie_python = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uxbdcqmd.json")

    # Отображаем анимированное изображение, если оно успешно загрузилось
    if lottie_python:
        st_lottie_spinner(lottie_python, height=300, key="python_animation")
    else:
        st.warning("Не удалось загрузить анимированное изображение.")

def show_chapter2():
    st.header("Зачем нужен Python?")
    with open("data/introduction/chapter2.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

    # Загружаем GIF-изображение
    st.image("https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif", use_column_width=True)

def show_chapter3():
    st.header("Установка Python")
    with open("data/introduction/chapter3.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

    # Загружаем видео с YouTube
    st_player("https://www.youtube.com/watch?v=8zhoR2xT5_I")  # Русскоязычное видео

def show_chapter4():
    st.header("Дополнительная тема 1")
    with open("data/introduction/chapter4.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def show_chapter5():
    st.header("Дополнительная тема 2")
    with open("data/introduction/chapter5.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def show_test(chapter):
    st.subheader(f"Тест по разделу '{chapter}'")
    # Добавьте здесь код для отображения теста

def update_user_data(username, chapter, test_result=None):
    import user_data  # Импортируем модуль user_data

    # Обновляем прогресс обучения пользователя
    user_data.update_progress(username, chapter)

    # Обновляем результаты теста пользователя
    if test_result is not None:
        user_data.update_test_result(username, chapter, test_result)

if __name__ == "__main__":
    show_content()

import streamlit as st

def show():
    # Загрузка содержимого из файла
    with open("functions_content.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # Отображение содержимого
    st.markdown(content, unsafe_allow_html=True)

    # Добавление теста и практических заданий
    # ... (код с тестами и заданиями) ...

"\""

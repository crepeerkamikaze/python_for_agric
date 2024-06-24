import streamlit as st
import bcrypt

# Функция для хеширования пароля
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Функция для регистрации нового пользователя
def register_user(username, password, user_data):
    # Проверяем, существует ли уже пользователь с таким именем
    if username in user_data.users:
        st.error("Пользователь с таким именем уже существует.")
        return False

    # Хешируем пароль
    hashed_password = hash_password(password)

    # Добавляем нового пользователя в словарь
    user_data.users[username] = {
        'password': hashed_password,
        'progress': {},
        'test_results': {}
    }

    st.success("Регистрация прошла успешно!")
    return True

# Функция для изменения пароля
def change_password(username, old_password, new_password, user_data):
    # Проверяем, существует ли пользователь
    if username not in user_data.users:
        st.error("Пользователь не найден.")
        return False

    # Проверяем старый пароль
    hashed_old_password = user_data.users[username]['password']
    if not bcrypt.checkpw(old_password.encode('utf-8'), hashed_old_password):
        st.error("Неверный старый пароль.")
        return False

    # Хешируем новый пароль
    hashed_new_password = hash_password(new_password)

    # Обновляем пароль пользователя
    user_data.users[username]['password'] = hashed_new_password

    st.success("Пароль успешно изменен!")
    return True

# Функция для проверки авторизации
def check_auth(user_data):
    # Получение пароля от пользователя
    password = st.text_input("Введите пароль", type="password")

    # Проверка пароля
    if hash_password(password) == st.secrets["textSweetPassword"]:
        return True
    else:
        return False

# Функция для отображения содержимого после авторизации
def show_content(username):
    # Импорт модулей с содержимым
    import introduction
    import basics
    import applications
    import advanced

    # Отображение содержимого
    # ... (код из app.py) ...

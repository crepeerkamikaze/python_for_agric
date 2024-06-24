import streamlit as st

def show_cabinet(username, user_data):
    st.title("Кабинет пользователя")

    if username:
        # Получаем прогресс обучения пользователя
        progress = user_data.get_progress(username)
        if progress:
            st.subheader("Прогресс обучения")
            for chapter, completed in progress.items():
                st.write(f"{chapter}: {'Пройдено' if completed else 'Не пройдено'}")

        # Получаем результаты тестов пользователя
        test_results = user_data.get_test_results(username)
        if test_results:
            st.subheader("Результаты тестов")
            for chapter, result in test_results.items():
                st.write(f"{chapter}: {result}")
    else:
        st.warning("Пожалуйста, авторизуйтесь для доступа к кабинету.")

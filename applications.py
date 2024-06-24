import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Применение Python в аграрных задачах")

    st.header("Обработка данных о урожайности")
    data = {
        "Год": [2020, 2021, 2022],
        "Урожайность (т/га)": [5.5, 6.2, 5.8]
    }
    df = pd.DataFrame(data)

    st.subheader("Импорт данных")
    st.code("df = pd.DataFrame(data)", language="python")

    st.subheader("Анализ данных")
    st.code("print(df.describe())", language="python")
    st.write(df.describe())

    st.subheader("Визуализация данных")
    plt.figure()
    plt.plot(df["Год"], df["Урожайность (т/га)"])
    plt.title("Динамика урожайности")
    plt.xlabel("Год")
    plt.ylabel("Урожайность (т/га)")
    st.pyplot(plt)

    st.header("Задание: Анализ данных")
    st.text("Представьте, что у вас есть данные о урожайности пшеницы за 5 лет:")
    data = {
        "Год": [2018, 2019, 2020, 2021, 2022],
        "Урожайность (т/га)": [4.8, 5.2, 5.5, 5.0, 4.9]
    }
    df = pd.DataFrame(data)
    st.subheader("Создайте график динамики урожайности.")
    code = st.text_area("Введите код", """
    import matplotlib.pyplot as plt
    # ... ваш код ...
    """)
    if st.button("Проверить"):
        try:
            exec(code)
            plt.show()
            st.pyplot(plt)
            st.success("График успешно создан!")
        except Exception as e:
            st.error(f"Ошибка: {e}")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Применение Python в аграрных задачах")

    st.header("Обработка данных о урожайности")
    data = {
        "Год": [2020, 2021, 2022],
        "Урожайность (т/га)": [5.5, 6.2, 5.8]
    }
    df = pd.DataFrame(data)

    st.subheader("Импорт данных")
    st.code("df = pd.DataFrame(data)", language="python")

    st.subheader("Анализ данных")
    st.code("print(df.describe())", language="python")

    st.subheader("Визуализация данных")
    plt.figure()
    plt.plot(df["Год"], df["Урожайность (т/га)"])
    plt.title("Динамика урожайности")
    plt.xlabel("Год")
    plt.ylabel("Урожайность (т/га)")
    plt.show()
    st.pyplot(plt)


    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def show():
    # ... (остальной код) ...
    st.header("Задание: Анализ данных")
    st.text("Представьте, что у вас есть данные о урожайности пшеницы за 5 лет:")
    data = {
        "Год": [2018, 2019, 2020, 2021, 2022],
        "Урожайность (т/га)": [4.8, 5.2, 5.5, 5.0, 4.9]
    }
    df = pd.DataFrame(data)
    st.subheader("Создайте график динамики урожайности.")
    code = st.text_area("Введите код", """
    import matplotlib.pyplot as plt
    # ... ваш код ... 
    """)
    if st.button("Проверить"):
        try:
            exec(code)
            plt.show()
            st.pyplot(plt)
            st.success("График успешно создан!")
        except Exception as e:
            st.error(f"Ошибка: {e}")
import streamlit as st

def show():
    st.header("Управляющие конструкции в Python")

    st.subheader("Условные операторы")
    st.write("Условные операторы позволяют выполнять различные блоки кода в зависимости от определенных условий.")
    st.code("""
    # Условный оператор if
    x = 10
    if x > 5:
        print("x больше 5")
    else:
        print("x меньше или равно 5")

    # Условный оператор if-elif-else
    age = 25
    if age < 18:
        print("Несовершеннолетний")
    elif age >= 18 and age < 65:
        print("Совершеннолетний")
    else:
        print("Пенсионер")
    """, language="python")

    st.subheader("Циклы")
    st.write("Циклы позволяют выполнять блок кода несколько раз.")
    st.code("""
    # Цикл for
    fruits = ["яблоко", "банан", "апельсин"]
    for fruit in fruits:
        print(fruit)

    # Цикл while
    count = 0
    while count < 5:
        print(count)
        count += 1

    # Оператор break
    for i in range(10):
        if i == 5:
            break
        print(i)

    # Оператор continue
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
    """, language="python")

    st.subheader("Викторина: Условные операторы")
    question = "Что будет выведено в результате выполнения следующего кода?"
    code = """
    x = 10
    y = 5
    """

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.header("Основы программирования на Python")

    st.subheader("Типы данных")
    st.write("Python поддерживает различные типы данных, такие как числа, строки, списки, кортежи, множества и словари.")
    st.code("""
    # Числа
    x = 5
    y = 3.14

    # Строки
    name = "Иван"

    # Списки
    fruits = ["яблоко", "банан", "апельсин"]

    # Кортежи
    coordinates = (10.5, 20.7)

    # Множества
    unique_fruits = set(["яблоко", "банан", "апельсин", "яблоко"])

    # Словари
    student = {"name": "Иван", "age": 20, "gpa": 4.2}
    """, language="python")

    st.subheader("Управляющие конструкции")
    st.write("Python поддерживает различные управляющие конструкции, такие как условные операторы и циклы.")
    st.code("""
    # Условный оператор
    age = 18
    if age >= 18:
        print("Совершеннолетний")
    else:
        print("Несовершеннолетний")

    # Цикл for
    fruits = ["яблоко", "банан", "апельсин"]
    for fruit in fruits:
        print(fruit)

    # Цикл while
    count = 0
    while count < 5:
        print(count)
        count += 1
    """, language="python")

    st.subheader("Функции")
    st.write("Функции позволяют организовать код в отдельные блоки и повторно использовать их.")
    st.code("""
    # Определение функции
    def square(x):
        return x ** 2

    # Вызов функции
    result = square(5)
    print(result)  # 25
    """, language="python")

    st.subheader("Викторина: Типы данных")
    question = "Какой тип данных подходит для хранения целых чисел?"
    options = ["int", "str", "list", "dict"]
    answer = st.multiselect("Выбери правильный ответ", options)

    if st.button("Проверить"):
        if "int" in answer:
            st.success("Правильно!")
        else:
            st.error("Неверно. Для хранения целых чисел используется тип данных int.")

    # Добавляем практическое задание
    st.subheader("Практическое задание")
    st.write("Напишите функцию, которая принимает список чисел и возвращает их сумму.")
    code = st.text_area("Введите код здесь", height=200)

    if st.button("Проверить задание"):
        try:
            sum_func = eval(code)
            numbers = [1, 2, 3, 4, 5]
            result = sum_func(numbers)
            if result == sum(numbers):
                st.success(f"Правильно! Сумма чисел {numbers} равна {result}.")
            else:
                st.error(f"Неверно. Ожидаемый результат: {sum(numbers)}.")
        except Exception as e:
            st.error(f"Ошибка: {e}")

def show_data_types():
    st.header("Переменные и типы данных")
    with open("basics/data_types.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def show_control_structures():
    st.header("Условные операторы")
    with open("basics/control_structures.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def show_loops():
    st.header("Циклы")
    with open("basics/loops.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def show_functions():
    st.header("Функции")
    with open("basics/functions.txt", "r", encoding="utf-8") as f:
        content = f.read()
    st.write(content)

def update_user_data(username, chapter, test_result=None, user_data=None):
    # Обновляем прогресс обучения пользователя
    if user_data is not None:
        user_data.update_progress(username, chapter)

    # Обновляем результаты теста пользователя
    if test_result is not None and user_data is not None:
        user_data.update_test_result(username, chapter, test_result)

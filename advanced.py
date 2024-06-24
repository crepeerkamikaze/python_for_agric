import streamlit as st

def show():
    st.title("Дополнительные темы")

    st.header("Объектно-ориентированное программирование")
    st.subheader("Классы")
    st.code("""
class Crop:
    def __init__(self, name, yield_per_hectare):
        self.name = name
        self.yield_per_hectare = yield_per_hectare

    def get_yield(self, area):
        return self.yield_per_hectare * area
    """, language="python")

    st.subheader("Объекты")
    st.code("wheat = Crop(\"Пшеница\", 6.0)", language="python")

    st.subheader("Наследование")
    st.code("""
class HybridCrop(Crop):
    def __init__(self, name, yield_per_hectare, hybrid_factor):
        super().__init__(name, yield_per_hectare)
        self.hybrid_factor = hybrid_factor

    def get_yield(self, area):
        return super().get_yield(area) * self.hybrid_factor
    """, language="python")

    st.subheader("Пример использования")
    wheat = Crop("Пшеница", 6.0)
    hybrid_wheat = HybridCrop("Гибридная пшеница", 7.0, 1.2)

    st.write(f"Урожайность обычной пшеницы на 10 га: {wheat.get_yield(10)} т")
    st.write(f"Урожайность гибридной пшеницы на 10 га: {hybrid_wheat.get_yield(10)} т")

    st.header("Работа с файлами")
    st.subheader("Чтение файла")
    st.code("""
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
    """, language="python")

    st.subheader("Запись в файл")
    st.code("""
with open("output.txt", "w") as file:
    file.write("Это пример записи в файл.")
    """, language="python")

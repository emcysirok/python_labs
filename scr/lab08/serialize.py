import json
import os
from .models import Student

def students_to_json(students: list[Student], path: str): # функция для сохранения списка студентов в json
    data = [student.to_dict() for student in students] # преобразуем каждый объект student в словарь с помощью метода to_dict()
    os.makedirs(os.path.dirname(path), exist_ok=True) # создаем папки по указанному пути, если они не существуют, exist_ok=True означает, что не будет ошибки если папка уже существует
    with open(path, 'w', encoding='utf-8') as f: # открываем файл для записи
        json.dump(data, f, ensure_ascii=False, indent=2) # ensure_ascii=False - разрешаем кириллицу, indent=2 - красивое форматирование с отступами
def students_from_json(path: str) -> list[Student]: # функция для загрузки списка студентов из json
    with open(path, 'r', encoding='utf-8') as f: # открываем файл для чтения
        data = json.load(f) # загружаем данные из json в переменную data
    students = []
    for item in data:
        student = Student.from_dict(item) # создаем объект student из словаря с помощью метода from_dict()
        students.append(student) 
    return students
from dataclasses import dataclass # для автоматического создания методов класса
from datetime import datetime, date # для работы с датами
@dataclass # декоратор автоматически создающий конструктор __init__ и другие методы
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    def __post_init__(self): # метод после конструктора __init__
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d") # пытаемся преобразовать строку в дату по указанному формату
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD") # если не получается - выбрасываем ошибку
        
        # ПРЕОБРАЗУЕМ GPA В FLOAT ЕСЛИ ОН СТРОКА
        if isinstance(self.gpa, str):
            try:
                self.gpa = float(self.gpa)
            except ValueError:
                raise ValueError(f"GPA должен быть числом, получено: {self.gpa}")
        
        if not (0 <= self.gpa <= 5): # проверка диапазона среднего балла
            raise ValueError(f"GPA должен быть от 0 до 5, получено: {self.gpa}")
    def age(self) -> int: # метод для вычисления возраста студента
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date() # преобразуем строку с датой рождения в объект date
        today = date.today() # получаем текущую дату
        age = today.year - birth_date.year # вычисляем разницу в годах
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day): # корректируем возраст, если день рождения в этом году еще не наступил
            age -= 1
        return age
    def to_dict(self) -> dict: # преобразование объекта в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    @classmethod # метод класса для создания объекта из словаря
    def from_dict(cls, data: dict): # создаем новый объект класса, передавая значения из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    def __str__(self): # метод для строкового представления объекта
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"
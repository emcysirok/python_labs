import csv
from pathlib import Path
import sys

sys.path.append(r'C:\Users\emcysirok\Desktop\python_labs\scr\lab08')
from models import Student

class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self):
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError()
            for row in reader:
                Student(**row)  
                rows.append(row)
        return rows

    def _write_all(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def is_empty(self):
        return len(self._read_all()) == 0

    def list(self):
        rows = self._read_all()
        return [Student(**r) for r in rows]

    def add(self, student):
        rows = self._read_all()
        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        self._write_all(rows)

    def find(self, substr):
        substr = substr.lower()
        rows = self._read_all()
        return [Student(**r) for r in rows if substr in r["fio"].lower()]

    def remove(self, fio):
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        self._write_all(new_rows)

    def update(self, fio, **fields):
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    if k in self.HEADER:
                        r[k] = v
                Student(**r)  
        self._write_all(rows)

    def stats(self):
        rows = self._read_all()
        if not rows:
            return {"count": 0, "average_gpa": 0, "top_5_students": []}
        gpas = [float(r["gpa"]) for r in rows]
        sorted_rows = sorted(rows, key=lambda x: float(x["gpa"]), reverse=True)
        return {
            "count": len(rows),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "top_5_students": sorted_rows[:5]
        }
    
if __name__ == "__main__":
    # Создаем группу
    group = Group("data/lab09/students.csv")
    
    # Очищаем файл для чистого теста
    if group.path.exists():
        group.path.unlink()
        
    group._ensure_storage_exists()
    # Добавляем студентов
    group.add(Student("Романенко Глеб", "2000-11-10", "БИВТ-21-3", 4.1))
    group.add(Student("Лобанов Семён", "2001-07-14", "БИВТ-21-2", 4.7))
    
    print(f"Изначально студентов: {len(group.list())}")
    print("Студенты:")
    for student in group.list():
        print(f"  - {student}")
    
    # Обновление
    group.update("Романенко Глеб", gpa=4.7, group="БИВТ-19-2")
    
    print(f"\nПосле обновления Романенко:")
    for student in group.list():
        print(f"  - {student}")
    
    # Удаление
    group.remove("Лобанов Семён")
    
    print(f"\nПосле удаления Лобанова, студентов: {len(group.list())}")
    print("Оставшиеся студенты:")
    for student in group.list():
        print(f"  - {student}")
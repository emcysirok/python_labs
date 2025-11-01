from pathlib import Path
import csv
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
"""
encoding: кодировка файла (по умолчанию "utf-8")
изменить кодировку: encoding="cp1251" 
"""
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    ensure_parent_dir(p)
    rows = list(rows)
    if rows: 
        dlina1 = len(rows[0])
        for stroka in rows:
            if len(stroka) != dlina1:
                raise ValueError("Все строки должны иметь одинаковую длину.")
        
    with p.open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)
def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    
    write_csv([("word", "count"), ("test", 3)], "data/result.csv")
    try:
        txt = read_text("scr/lab04/input.txt")
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print("Файл input.txt не найден")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла")
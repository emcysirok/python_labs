from collections import Counter
import re
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
    
    try:
        txt = read_text("input.txt")
        words = re.findall(r'\w+', txt.lower())
        counts = Counter(words)
        sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        write_csv(sorted_words, "report.csv", header=("word", "count"))
        
        print(f"Всего слов: {sum(counts.values())}")
        print(f"Уникальных слов: {len(counts)}")
        print("Топ-5:")
        for word, count in sorted_words[:5]:
            print(f"{word}:{count}")
            
    except FileNotFoundError:
        print("Файл input.txt не найден")
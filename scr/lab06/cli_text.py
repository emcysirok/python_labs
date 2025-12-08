import argparse
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))  # папка lab06
project_root = os.path.dirname(os.path.dirname(current_dir))  # папка python_labs
sys.path.insert(0, project_root)  # добавляем путь к проекту

from scr.lib.text import *

def cat(text, n):
    # открытие и чтение файлаа
    with open(text, "r", encoding='utf-8') as file:
        lines = file.readlines()
    
    # вывод строки файла
    if not n:
        for line in lines:
            print(line.rstrip('\n'))
    else:
        # нумер строк
        for i, line in enumerate(lines, 1):
            print(f"{i} {line.rstrip('\n')}")

def stats(txt, n):
    # чит содержимое файла
    with open(txt, "r", encoding='utf-8') as file:
        content = file.read()
    
    result = top_n(count_freq(tokenize(normalize(content))), n)
    
    print(f"топ-{n} слов:")
    for word, count in result:
        print(f"'{word}' - {count} раз")

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")

subparsers = parser.add_subparsers(dest="command")

cat_parser = subparsers.add_parser("cat", help="вывести содержимое файла")
cat_parser.add_argument("--input", required=True)
cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

stats_parser = subparsers.add_parser("stats", help="частоты слов")
stats_parser.add_argument("--input", required=True)
stats_parser.add_argument("--top", type=int, default=5)

# разбир аргументы
args = parser.parse_args()

# выполн команду
if args.command == "cat":
    cat(args.input, args.n)

if args.command == "stats":
    stats(args.input, args.top)
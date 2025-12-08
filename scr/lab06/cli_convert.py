import argparse
import sys
from scr.lab05.csv_xlsx import csv_to_xlsx
from scr.lab05.json_csv import json_to_csv, csv_to_json

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6") # создаем главный парсер 
subparsers = parser.add_subparsers(dest="command", required=True) # добавляем подпарсеры для разных команд
# dest="command" сохраняет выбранную команду в args.command
# required=True обязательна (иначе покажет help)

json2csv_parser = subparsers.add_parser("json2csv")  # создаем подпарсер
json2csv_parser.add_argument("--in", required=True, dest='input')  # добавляем обязательный аргумент --in
# dest='input' переименовывает его в args.input
json2csv_parser.add_argument("--out", required=True)  # добавляем обязательный аргумент --out для выходного файла

csv2json_parser = subparsers.add_parser("csv2json")
csv2json_parser.add_argument("--in",required=True,dest='input')  # обязательный входной файл (--in → args.input)
csv2json_parser.add_argument("--out",required=True) # обязательный выходной файл

csv2xlsx_parser = subparsers.add_parser("csv2xlsx")
csv2xlsx_parser.add_argument("--in",required=True,dest='input') # входной файл csv
csv2xlsx_parser.add_argument("--out",required=True) # выходной файл xlsx

args = parser.parse_args() # парсим аргументы командной строки, переданные при запуске программы

# try/except для обработки ошибок
try:
    if args.command == "json2csv":
        json_to_csv(args.input, args.out)
        print(f"json → csv: {args.input} → {args.out}")

    if args.command == "csv2json":
        csv_to_json(args.input, args.out)
        print(f"csv → json: {args.input} → {args.out}")

    if args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.out)
        print(f"csv → xlsx: {args.input} → {args.out}")

except Exception as e:
    print(f"ошибка: {e}")
    sys.exit(1)

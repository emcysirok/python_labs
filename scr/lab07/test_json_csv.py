import pytest
import json
import csv
import os
from scr.lab05.json_csv import json_to_csv, csv_to_json

def run_in_tmp(func, tmp_path, src, dst):
    """запускает функцию с относительными путями в tmp_path"""
    os.chdir(tmp_path)
    try:
        func(src, dst)
    finally:
        os.chdir("..")

# поз тесты
def test_json_to_csv_ok(tmp_path):
    with open(tmp_path / "test.json", "w") as f:
        json.dump([{"name": "Alice", "age": 25}], f)
    
    run_in_tmp(json_to_csv, tmp_path, "test.json", "out.csv")
    
    with open(tmp_path / "out.csv") as f:
        rows = list(csv.DictReader(f))
        assert len(rows) == 1
        assert rows[0]["name"] == "Alice"

def test_csv_to_json_ok(tmp_path):
    # csv должен содержать данные а не тольк заголовок
    with open(tmp_path / "test.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Bob", "age": "30"})
    
    run_in_tmp(csv_to_json, tmp_path, "test.csv", "out.json")
    
    with open(tmp_path / "out.json") as f:
        result = json.load(f)
        assert len(result) == 1
        assert result[0]["name"] == "Bob"

# нег тесты
def test_json_to_csv_wrong_path(tmp_path):
    os.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        json_to_csv("no.json", "out.csv")
    os.chdir("..")

def test_csv_to_json_wrong_path(tmp_path):
    os.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        csv_to_json("no.csv", "out.json")
    os.chdir("..")

def test_json_to_csv_empty(tmp_path):
    (tmp_path / "empty.json").write_text("")
    os.chdir(tmp_path)
    with pytest.raises(ValueError):
        json_to_csv("empty.json", "out.csv")
    os.chdir("..")

def test_csv_to_json_empty(tmp_path):
    (tmp_path / "empty.csv").write_text("")
    os.chdir(tmp_path)
    with pytest.raises(ValueError):
        csv_to_json("empty.csv", "out.json")
    os.chdir("..")

# round-trip с учётом того что csv всё сохраняет как строки
def test_round_trip(tmp_path):
    # Исходные данные
    data = [{"a": 1, "b": 2}]
    
    # JSON → CSV
    (tmp_path / "1.json").write_text(json.dumps(data))
    os.chdir(tmp_path)
    json_to_csv("1.json", "data.csv")
    csv_to_json("data.csv", "2.json")
    os.chdir("..")
    
    with open(tmp_path / "2.json") as f:
        result = json.load(f)
    
    # в csv всё становится строками поэтому после цикла получаем строки
    assert result == [{"a": "1", "b": "2"}]
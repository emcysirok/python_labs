import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lab03.lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

def main():
    input_file = "input.txt"
    output_file = "report.csv"

    try:
        text = read_text(input_file)
        print(f"файл {input_file} прочитан")
    
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        freq = count_freq(tokens)
        
        all_sorted_words = top_n(freq, len(freq))
        write_csv(all_sorted_words, output_file, header=("word", "count"))
        print(f"сохранено в {output_file}")
        
        total_words = len(tokens)
        unique_words = len(freq)
        
        print(f"всего слов: {total_words}")
        print(f"уникальных слов: {unique_words}")
        
        top_5_words = top_n(freq, 5)
        print("Топ-5:")
        for word, count in top_5_words:
            print(f"{word}:{count}")
            
    except FileNotFoundError:
        print(f"файл {input_file} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
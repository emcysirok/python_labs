import sys
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    # Используем тестовый текст напрямую
    text = "Привет, мир! Привет!!!"
    
    # Обрабатываем текст
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    # Выводим результаты
    print(f"всего слов: {len(tokens)}")
    print(f"уникальных слов: {len(freq)}")
    print("топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
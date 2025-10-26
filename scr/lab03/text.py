import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё','е').replace('Ё','E')
    text = text.replace("\n", " ").replace("\t", " ").replace("\r", " ")
    while '  ' in text:
        text = text.replace('  ',' ')
    return text.strip()
print("normalize:")
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные  пробелы  "))

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)
print("")
print("tokenize:")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq= {}
    for w in tokens:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq
print("")
print("count_freq:")
print(count_freq(["a","b","a","c","b","a"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort()
    items.sort(key=lambda x: x[1],reverse=True)
    return items[:n]
print('')
print('top_n:')
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2))

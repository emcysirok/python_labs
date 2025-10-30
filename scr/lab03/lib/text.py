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

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for w in tokens:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]
def histogram(word: str) -> dict[str, int]:
    import string
    abc = string.ascii_lowercase

    map = {}
    for char in abc:
        map[char] = word.lower().count(char)
    return map

print(histogram("Alabama is a town"))
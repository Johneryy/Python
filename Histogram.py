def histogram(word: str) -> dict[str, int]:
    import string
    abc = string.ascii_lowercase

    map = {}
    for char in abc:
        map[char] = word.lower().count(char)
    return map

def histogram2(word):
    import string
    return {char: word.lower().count(char) for char in string.ascii_lowercase}

print(histogram2("I prefer Java to python"))

def uniquevalues(word: str) -> int:
    return len(set(word))
print(uniquevalues("Alabama is on"))
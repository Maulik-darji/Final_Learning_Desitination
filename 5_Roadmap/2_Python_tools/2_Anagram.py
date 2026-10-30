from collections import Counter
def anagram(string1 : str, string2: str) -> bool:
    return Counter(string1) == Counter(string2)

print(anagram('listen', 'silent'))

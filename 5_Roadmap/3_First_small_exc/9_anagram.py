from collections import Counter

def anagram(x: str, y: str)-> bool:
    return Counter(x) == Counter(y)

print(anagram("silent", "listen"))
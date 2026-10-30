from collections import Counter

def anagram(string1: str, string2: str) -> bool:
    count1 = Counter(string1)
    count2 = Counter(string2)

    for i in count1:
        if count1[i] != count2[i]:
            return False

        return count1.keys() == count2.keys()
    
print(anagram("listen", "silent"))
print(anagram("hello", "world"))
print(anagram("aabb", "abab"))
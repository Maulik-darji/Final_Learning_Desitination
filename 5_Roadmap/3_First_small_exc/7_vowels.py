# text = "Hello Maulik Darji"

# count = 0

# for char in text:
#     if char.lower() in "aeiou":
#         count+=1
# print(count)

# #code2 using split()
# text = "Python is easy to learn"
# words = text.split()
# print(words)
# print("Total Words", len(words))

text = "Maulik was born on 13th june"

vowel = 0
word = 0
number = 0

for i in text:
    if i.lower() in "aeiou":
        vowel += 1

    if i.isdigit():
        number+=1
word = len(text.split())

print("Number of Vowels: ", vowel)
print("Number of Word: ", word)
print("Number of number: ", number)
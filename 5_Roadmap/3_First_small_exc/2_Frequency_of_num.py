from collections import Counter

list1 = [10, 20, 20, 30, 10, 30, 40, 30, 30, 50, 60]

count = Counter(list1)
print(count)

# Printing Frequency of Number 40
print(count[30])

#printing frequency of largest number
def largest(list1):
    largest = list1[0]
    for number in list1:
        if number > largest:
            largest = number
    frequency = count[largest]
    print("Maximum: ", largest, "Frequency: ", frequency)
    
print(largest(list1))

#printint frequency of characte of word
name = "Maulik Darji"
countfre = Counter(name)

for i, fre in countfre.items():
    print(i, ":", fre)

print(*countfre.items(), sep="\n")
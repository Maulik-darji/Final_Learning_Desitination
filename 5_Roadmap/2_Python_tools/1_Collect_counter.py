from collections import Counter

num = [10, 20, 20, 50, 30, 40, 50, 60]
count = Counter(num)
print(count)

name = "Maulik Darji"

print(Counter(name))

#To print the frequency of certain number.
print(count[20])
print(Counter(num)[20])


number2 = [20, 20, 20, 20, 20, 20, 50, 50, 20, 10, 10, 30, 30, 30, 70, 90]

count = Counter(number2)
print(count.most_common(5))
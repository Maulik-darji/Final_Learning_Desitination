from collections import Counter

numbers = [7, 2, 10, 12, 11]

target = 9

frequency = Counter(numbers)

for number in numbers:
    required = target - numbers
    if frequency[required] > 0:
        print(numbers, required)
        break
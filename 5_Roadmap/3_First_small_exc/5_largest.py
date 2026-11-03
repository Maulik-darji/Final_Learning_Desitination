list1 = [10, 20, 40, 1, 2, 5, 100]

largest = list1[0]

for i in list1:
    if i > largest:
        largest = i

print("Largest Number: ", largest)

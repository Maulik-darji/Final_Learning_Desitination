#code1 with set.

list = [10, 20, 30, 40, 50, 50, 20, 40, 60]
print(sorted(set(list)))

#code2 without set
unique = []

for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
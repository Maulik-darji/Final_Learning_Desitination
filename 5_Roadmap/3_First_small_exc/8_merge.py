list1 = [10, 20, 30, 50, 90]
list2 = [20, 40, 100, 2, 5]

for i in list2:
    list1.append(i)
print(sorted(list1))

#code 2 using merged
merged = list1 + list2
print(merged)
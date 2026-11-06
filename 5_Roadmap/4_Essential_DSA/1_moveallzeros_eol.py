list1 = [10, 0, 20, 0, 30, 0, 40, 0, 10, 1, 0]

list2 = []

for i in list1:
    if i != 0:
        list2.append(i)
for i in list1:
    if i==0:
        list2.append(i)
print(list2)

#code 2 without new list
list3 = [10, 0, 20, 0, 0, 40, 1, 2, 3, 5]
index = 0

for i in range(len(list3)):
    if list3[i] != 0:
        list3[index] = list3[i]
        index += 1
while index < len(list3):
    list3[index] = 0
    index +=1
print(list3)
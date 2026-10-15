list1 = ["Apple", "Banana", "Mango", "Guava", "Lichi"]

#indexing
print(list1[1])
print(list1.index("Banana"))



#slicing
print(list1[1:5])
print(list1[1:5:2])



#inserting
list1.append("Coconut")
print(list1)

list1.insert(1,"Coconut")
print(list1)



#Removing Duplicate
print(set(list1))
unique = list(dict.fromkeys(list1))
print(unique)

print(list(dict.fromkeys(list1)))


#Removing or deleteing
indexing = 0
list1.pop(indexing)
print(list1)

#printing index
indexcheck = (list1.index("Banana"))
list1.pop(indexcheck)
print(list1)

del list1[0]
print(list1)

#Copying the list

originalist = [10,20,30,40]
copied = originalist.copy()
copied.append(100)
print(originalist)
print(copied)
strn = "Maulik"
print(strn[::-1])

#method 2
print("Using for loop:")
for i in strn[::-1]:
    print(i)

#method 3

print("Using Reversed: ", reversed(strn))

print("Using Join:", "".join(reversed(strn)))
#reversing list
list1 = [10, 20, 30, 40, 50]
print(list1[::-1])
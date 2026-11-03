list1 = [10,20,30,40,50,100,2,3,5]

largest = float('-inf')
secondlargest = float('-inf')

for i in list1:
    if i>largest:
        secondlargest = largest
        largest = i
    elif i>secondlargest and i != largest:
        secondlargest = i

print("Second Largest Number: ", secondlargest)
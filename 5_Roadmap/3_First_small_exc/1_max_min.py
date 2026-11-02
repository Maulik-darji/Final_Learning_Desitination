# code 1
mylist = [2, 10, 11, 1, 5, 20]

smales = mylist[0]
largest = mylist[0]
for number in mylist:
    if number < smales:
        smales = number

    if number > smales:
        largest = number

print("Maximum: ", largest)
print("Minimum: ",  smales)

"""
Time complexity
min() and max() = O(n) combined 
Extra Space O(1)

Manual Loop Time complexity - O(n)
Extra Space O(1) 
"""
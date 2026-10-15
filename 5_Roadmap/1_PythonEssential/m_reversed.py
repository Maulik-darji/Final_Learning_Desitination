listrev = ["Mango", "Apple", "Kiwi", "Jackfruit", "Noice"]
for i in reversed(listrev):
    print(i)

listnex = ["Cat", "Dog", "Cow", "Crow", "Bear"]

for i, j in zip(listrev, listnex):
    print(i,j)
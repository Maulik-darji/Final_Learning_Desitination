stringname = "Maulik Darji"


#1. Indexing
print(stringname.index('a'))
print(stringname[0])

#2.Slicing
print(stringname[1:5])
print(stringname[0:13:2])
print(stringname[:12])
print(stringname[::-1])
print(stringname[2::-1])

#3. Joining 
name = "Maulik"
Surname = "Darji"
print(name+" "+Surname)

def greet(name, surname):
    print("Good Morning ", name+" "+surname)
greet("Maulik", 'Darji')

#4. 
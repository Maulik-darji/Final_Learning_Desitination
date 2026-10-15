# tuple unpacking = Tuple unpacking means assigning the values inside a tuple to separate variables in one statement.
student = ("Maulik", 21, "CSE")
name, age, branch = student

print(name)
print(age)
print(branch)

#swapping two variables using unpacking.

a = 100
b = 200
c = 300

a,b,c = c,a,b
print(a)
print(b)
print(c)

#unpacking with * operator
num = (10,20,30,40,50,60,70,80,90,100)

*first, second, last = num
print(first)
print(second)
print(last)

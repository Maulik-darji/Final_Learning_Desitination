# string1 = "My Name is Maulik"

# print(string1.index("is"))

# print(string1.index("Hello"))

# print(string1.find("Hello"))


#-----------Strip()-------------
# string2 = input("Enter Name: ")
# string2 = string2.strip("-")
# string2 = string2.strip(" ")
# print(string2)

# #-----------Split()-------------
# string3 = ("My Name is Maulik")
# print(string3.split("a"))

#-------------Questin------------
input1 = "The Syk is Blue"
input1 = input1.split(" ")[::-1]
input1 = " ".join(input1)
# input1 = input1[::-1]

print(input1)
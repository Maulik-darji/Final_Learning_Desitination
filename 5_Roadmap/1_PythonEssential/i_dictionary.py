student = {
    "name": "Maulik",
    "age": 21,
    "branch": "CSE"
}

print(student)

#Creating using dict

student_2 = dict(Name = "Maulik", Surname = "Darji", age = 21, city = "Ahmedabad")
print(student_2["Name"], student_2["age"])


#adding or editing 

student["city"] = "Ahmedabad"
print(student)
#using update
student.update({
    "city":"Banglore",
    "age": 22
})
print(student)

#Membership
student1 = {
    "name": "Maulik",
    "age": 21, 
    "City": "Ahmedabad"
}

print("name" in student1)

#Iteration
for i in student:
    print(i)

for i in student.values():
    print(i)

for i,j in student.items():
    print(i," - ",j)

from collections import defaultdict

numbers = [10, 20, 10, 30, 10]

count = defaultdict(int)

for num in numbers:
    count[num] +=1 
print(count)

#code2

students = [
    ("Maulik", "Python"),
    ("Rahul", "Java"),
    ("Amit", "Python"),
    ("Purv", "Java"),
    ("Nihar", "Go")
]

groups = defaultdict(list)

for name, subject in students:
    groups[subject].append(name)

print(dict(groups))


#code3

students2 = [
    ("Maulik", "Python"),
    ("Maulik", "Python"),
    ("Rahul", "Java"),
    ("Amit", "Python"),
    ("Purv", "Java"),
    ("Nihar", "Go")
]

groups2 = defaultdict(set)

for nam, sub in students2:
    groups2[sub].add(nam)
print(dict(groups2))
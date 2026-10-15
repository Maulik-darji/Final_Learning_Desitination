list1 = ["Maulik", "Khushi", "Purv", "Shivam", "Yug", "Darshan"]

result = sorted(list1, key=len, reverse=True)
print(result)
result = sorted(list1, key=len, reverse=False)
print(result)
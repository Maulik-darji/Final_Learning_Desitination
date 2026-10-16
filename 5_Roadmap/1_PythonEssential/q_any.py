nums = [2, 5, 6, 1, 10]

print(any(num < 5 for  num in nums))
print(any(num>5 for num in nums))
print(any(nums))
print(any(num>10 for num in nums))
from bisect import bisect_right, bisect_left

numbers = [10, 20, 35, 45, 50, 60]

print(bisect_left(numbers, 41))
print(bisect_right(numbers, 90))
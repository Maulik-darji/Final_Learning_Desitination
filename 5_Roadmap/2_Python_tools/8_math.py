import math

result = math.gcd(12, 36, 24)
print(result)

result2 = math.isqrt(30)
print(result2)


numbers = [50, 20, 80, 10, 40]
smallest = math.inf
for num in numbers:
    if num<smallest:
        smallest=num
print(smallest)


#code 3
students = 11
capacity = 4
cars = math.ceil(students/capacity)
print(cars)
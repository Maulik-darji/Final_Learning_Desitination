numbers: list[int] = [10, 20, 30, 40]

print(numbers)
print(numbers[0])

def calculate_sum(numbers: list[int]) -> int:
    return sum(numbers)

print(calculate_sum([10,20,30]))

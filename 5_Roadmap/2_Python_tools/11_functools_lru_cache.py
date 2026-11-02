from functools import lru_cache

@lru_cache(maxsize=3)
def square(number):
    print("Calculating...")
    return number*number

print(square(2))
print(square(3))


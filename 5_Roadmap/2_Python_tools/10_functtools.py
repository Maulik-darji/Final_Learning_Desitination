from functools import cache

@cache
def square(number):
    print("calculating...")
    return number*number

print(square(5))
print(square(5))
print(square(10))

# code.2 fibonaci using decorator.
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(9))

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))


from itertools import combinations, permutations, accumulate
from operator import mul
number = [10, 20, 30, 40]

result = combinations(number, 2)
print(list(result))

result_per = permutations(number, 2)
print(list(result_per))
#we need to use list becase combiantion, permutation and other provide iterator and we need to convert them to see to see all the results

result_acc = accumulate(number)
print(list(result_acc))

result_acc2 = accumulate(number, mul)
print(list(result_acc2))
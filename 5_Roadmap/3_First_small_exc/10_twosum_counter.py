from collections import Counter

list1 = [2, 7, 10, 11, 12, 15]
print("List: ", list1)
target = int(input("Enter Target Value: "))

freq = Counter(list1)

for num in list1:
    complement = target - num
    if freq[complement]>0:
        print("Two Sum Numbers are: ",  num, complement, sep=",")
        break
    freq[num] -= 1
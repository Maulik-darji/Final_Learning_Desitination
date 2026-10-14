list1 = [1,2,1,2,4,6,2,6,2,1,5,2]

freq = {}

for i in list1:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

for i in freq:
    print(f"{i} is present {freq[i]} times")
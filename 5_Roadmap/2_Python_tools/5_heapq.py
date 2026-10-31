import heapq

numbers = [10, 50, 5, 2, 70, 100]

heapq.heapify(numbers)
print(numbers)

# code 2
heapq.heappush(numbers, 3)
print(numbers)

# code 3

# while numbers:
#     current = heapq.heappop(numbers)
#     if current == 50:
#         break
# print(numbers)

#code 4
heapq.heappop(numbers)
print(numbers)

heapq.heappop_max(numbers)
print(numbers)

#code 4
numbers1 = [10, 30, 40, 50, 5, 2]
max_heap = []
for num in numbers1:
    heapq.heappush(max_heap, -num)

print(max_heap)

#code 5 to get largest number
largest = -heapq.heappop(max_heap)
print(largest)

#code 6
nums = [10, 20, 2, 100]
smallest = heapq.heap[0]
print(smallest)
string1 = "AAMMAA"

reverse = string1[::-1]
print(reverse)

if string1 == reverse:
    print("String is Palindrome")

#its time complexity can't be reduced but its space complexity can be optimized using two pointer method

#code 2
left = 0
right = len(string1) - 1

is_palindrome = True

while left < right:
    if string1[left] != string1[right]:
        is_palindrome = False
        break
    left +=1
    right -=1 
if is_palindrome:
    print("String is palindrome")
else:
    print("String is Not Palindrome")
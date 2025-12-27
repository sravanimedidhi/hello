
numbers = [3, 7, 2, 9, 4, 1, 8]
maximum = minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)


def find_max_min(arr):
    # if not arr:
    #     return None, None  

    max_val = min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

# Test the function
numbers = [3, 7, 2, 9, 4, 1, 8]
maximum, minimum = find_max_min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)









#Reverse an array in place
arr = [1, 2, 3, 4, 5]

# In-place swapping
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)
















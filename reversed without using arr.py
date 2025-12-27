# def reverse_array(arr):
#     return arr[::-1]

# # Example
# arr = [1, 2, 3, 4, 5]
# print("Reversed array:", reverse_array(arr))









def duplicated_element(arr):
    list = []
    for i in arr:
        for i in list:
            return True
        list.append(i)
        return False
arr=[1,2,3,4,5,6,7,8,9,1]
print("contains duplicate:",duplicated_element(arr))







def second_largest(arr):
    first = second = float('-inf')   # very small numbers

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

# Example
arr = [10, 20, 4, 45, 99]
print("Second largest:", second_largest(arr))









def intersection(arr1, arr2):
    result = []
    for num in arr1:
        if num in arr2 and num not in result:
            result.append(num)
    return result

# Example
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]

print("Intersection:", intersection(arr1, arr2))



text = "python"
rev = ""
i = len(text) - 1

while i >= 0:
    rev += text[i]
    i -= 1

print(rev)

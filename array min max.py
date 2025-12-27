# arr=[12,52,34,12,78,34,23,45]
# maxmimum=minium=arr[0]
# for num in arr:
#     if num>minium:
#         minium=num
#     if num<maxmimum:
#         maxmimum=num
# print("maximum,minimum:",maxmimum,minium)







def min_max(arr):
    maximum = minimum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum
arr = [12, 52, 34, 12, 78, 34, 23, 45]
maximum, minimum = min_max(arr) 
print("Maximum:", maximum)
print("Minimum:", minimum)








s = "madam"
is_pal = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        is_pal = False
        break

if is_pal:
    print("Palindrome")
else:
    print("Not a palindrome")



        
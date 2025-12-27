#Ask the user to enter the list of items using list comprehension and also accept the search element. traverse across ev
l1=[int(x) for x in input("Enter the element in list:").split()]
key=int(input('Enter the element to be searched:'))
for i in range(len(l1)):
    if l1[i] == key:
        print(f" the element{key} is found ar {i}")
        break
else:
    print(f"the element{key} is not found in the list")








   


#empty commit
#to perform binary search : list element should be sorted,find the middle element,compare the middle element with search
lst=list(map(int, input("Enter sorted list element:").split()))
key=int(input("Enter the element to search for: "))
low = 0
high = len(lst) - 1
found = False
while low <= high:
    mid =(low + high) // 2
    if lst[mid] == key:
        found = True
        break
    elif key < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1
if found:
    print(f"Element {key} found at index {mid}.")
else:
    print(f"Element {key} not found in the list.")
    




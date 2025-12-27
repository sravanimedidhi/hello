# //write a factorial functionin python using for loop
def factorial(n):
    result = 1
    for i in range(1,n):
        result *=i
        return result
n=int(input("Enter n value:"))
result = factorial(n)
print(f"factorial of {n} is {result}")
   






def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i

    return result
for x in range(1,11):
    print(f"factorial of {x} is {factorial(x)}")






# def factorial(n):
#     result = 1
#     while n > 1:
#         result *=n
#         n -=1
#         return result
#     n=int(input("Enter n value:"))
#     result = factorial(n)
#     print(f"factorial of {n} is {result}")









    num = 1
    while num <=10:
        print(num)
        num+=1
# def fact(n):
#     res = 1
#     while res <= n:
#         res*=1
#         return res
#     n=int(input("Enter n value:"))
#     result = fact(n)
#     print(f"fact of {n} is {res}")





def factorial_while(n):
    # if n < 0:
    #     return "Factorial is not defined for negative numbers."
    
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1
    
    return result
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial_while(num)}")




def fact(n):
    res = 1
    i = 1
    while i < n + 1:
        res *= i
        i += 1
    return res  # Make sure return is outside the while loop

for x in range(1, 11):
    print(f"fact of {x} is {fact(x)}")

    

        


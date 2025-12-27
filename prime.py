
    
for num in range(2, 30):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False           
            break
    if is_prime:
        print(num)



n = int(input("Enter a prime number"))
print(" prime number are:")
for n in  range(n+1):
    if n>1:
      for i in range(2,n):
        if n % i == 0:
            break
        else:
            print(n)








#wite a program to find n numbers prime number 10
n=int(input("Enter the number:"))
count=0
num=2
while count<n:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=" ")
        count+=1
    num+=1





year=int(input("Enter the year:"))
if(year%400==0):
    print(f"(year) is a leap year")
else:
    print(f"(year) is not a leap year")











#define a function prime() which take a numbers and prints whether it is prime or not

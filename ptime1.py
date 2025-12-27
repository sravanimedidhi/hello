n = int(input("Enter a prime number"))
print(" prime number are:")
for n in  range(n+1):
    if n>1:
      for i in range(2,n):
        if n % i == 0:
            break
        else:
            print(n)






def prime(n):
   if n>1:
      for i in range(2,n):
         if n%i==0:
            print("number is not prime number")
            break
         else:
            print("number is prime number")






def sum(a,b):
   c=a+b
   print(c)
x=10
y=15
sum(x,y)
   
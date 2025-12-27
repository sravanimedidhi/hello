#write a programm to print odd numbers from 100 to 1
for num in range(100, 0, -1):
    if num % 2 != 0:
        print(num)

for num in range(100, 0, -1):
    if num % 2 == 0:
        print(num)
#write
# a program to print muthiples of 6 from 100 to 1
for num in range(100, 0, -1):
    if num % 6 == 0:
        print(num)
#write a program to print multiplication table for given numbers 
n=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}") 
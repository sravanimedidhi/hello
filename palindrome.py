s="madam"
is_pal= True
for  i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        is_pal= False
        break
if is_pal:
    print("Palindrome")     
else:
    print("Not a Palindrome")





def is_palidrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False                
    return True
print(is_palidrome("madam"))
















def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar"))








def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))















s = input("Enter a string: ")

vowels = "aeiouAEIOU"

for char in s:
    if char in vowels:
        print(char)









s = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


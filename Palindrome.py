num=int(input("Enter any number: "))
n=num
res=0
while num>0:
    rem=num%10
    res=rem+res*10
    num=num//10
if res==n:
    print("Palindrome")
else:
    print("Not palindrome")

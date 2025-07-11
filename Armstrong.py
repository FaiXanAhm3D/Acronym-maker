num=input("Enter any number")
length=len(num)
n=int(num)
num=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**length
    n=n//10
if num==sum:
    print("yes")
else:
    print("no")

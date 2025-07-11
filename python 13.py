a=int(input("Enter any number :"))
b=int(input("Enter any number :"))
c=int(input("Enter any number :"))
if a>b and a>c:
    print(a," is the largest number")
elif b>a and b>c:
    print(b," is the largest number")
elif c>a and c>b:
    print(c," is the largest number")
elif a==b and b==c:
    print(a," is the largest number")
elif a==b and a>c:
    print(a," is the largest number")
elif b==c and b>a:
    print(b," is the largest number")
elif a==c and a>b:
    print(a," is the largest number")

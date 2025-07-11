#Making of a calculator
a=int(input("Enter first number= "))
o=input("Enter operator (+,-,*,/,%) = ")
b=int(input("Enter second number= "))
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
elif o=="*":
    print(a*b)
elif o=="/":
    print(a/b)
elif o=="%":
    print(a%b)
elif o=="//":
    print(a//b)
else:
    print("Invalid input")

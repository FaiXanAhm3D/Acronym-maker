def fibo():
    n=int(input("Enter the number of terms: "))
    first=0
    second=1
    print(first,second,end=" ")
    while n>=3:
          third=first+second
          print(third,end= " ")
          first=second
          second=third
          n=n-1
def add():
    x=int(input("Enter any numebr: "))
    y=int(input("Enter any number: "))
    print(x+y)
def sub():
    x=int(input("Enter any numebr: "))
    y=int(input("Enter any number: "))
    print(x-y)
def add():
    x=int(input("Enter any numebr: "))
    y=int(input("Enter any number: "))
    print(x/y)
add()




        

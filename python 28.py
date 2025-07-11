def checkNumber(N):
    status = N%2
    return status
#main-code
num=int(input(" Enter a number to check :"))
k=checkNumber(num)
if k == 0:
    print("This is EVEN number")
else:
    print("This is ODD number")

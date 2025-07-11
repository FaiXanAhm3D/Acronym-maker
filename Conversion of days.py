a=int(input("Number of days = "))
Y=a//365
M=(a%365)//30
W=((a%365)%30)//7
D=((a%365)%30)%7
print("No. of years = ",Y)
print("No. of months = ",M)
print("No. of weeks = ",W)
print("No. of days = ",D)

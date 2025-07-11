def AddOddEven(values):
    even_sum=0
    odd_sum=0
    for i in values:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    print(f"Even sum: {even_sum}")
    print(f"Odd sum: {odd_sum}")

lst=[]
while True:
    num=int(input("Enter either odd or even number: "))
    lst.append(num)
    cont=input("Do you want to continue y/n ")
    if cont=='n':
        break
    else:
        continue
AddOddEven(lst)

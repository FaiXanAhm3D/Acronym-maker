def HowMany(ID,Val):
    count=0
    for i in ID:
        if Val==i:
            count+=1
        else:
            continue
    print(f"{val} found {count} times")
lst=[]
while True:
    ID=int(input("Enter the ID: "))
    lst.append(ID)
    cont=input("Add more y/n: ")
    if cont=='n':
        break
    else:
        continue
val=int(input("Enter Val: "))
HowMany(lst,val)

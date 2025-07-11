def Push3_5(N):
    lst=[]
    for i in N:
        if i%5==0 or i%3==0:
                lst.append(i)
    return lst

NUM=[]
for i in range(5):
    a=int(input("Enter a number: "))
    NUM.append(a)
print(f"List of all the numbers: {NUM}")
Only3_5=Push3_5(NUM)
print(f"Numbers divisible by 3 or 5: {Only3_5}")

for i in range(len(Only3_5)):
    b=Only3_5.pop()
    print(b,end=" ")
    if Only3_5==[]:
        print("StackEmpty")

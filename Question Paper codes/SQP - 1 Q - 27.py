n=int(input("Enter upper limit: "))
lst=[]
for i in range(2,n+1):
    count=0
    if i==2:
        lst.append(i)
    else:
        for j in range(2,n):
            if i%j==0:
                count+=1
            if count==0:
                lst.append(i)
            else:
                continue
print(lst)

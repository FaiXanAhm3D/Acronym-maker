L=[1,2,3,4,5]
Lst=[]
for i in range(len(L)):
    if i%2==1:
        t=(L[i],L[i]**2)
        Lst.append(t)
print(Lst)

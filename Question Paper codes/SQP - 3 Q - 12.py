def listchange():
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]==l[i]*2
        if l[i]%3==0:
            l[i]=l[i]*3
        else:
            l[i]=l[i]*5
l=[2,6,9,10]
listchange()
for i in l:
    print(i,end='#')

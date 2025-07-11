a={}
a[1]=1
a['1']=2
a[1]=a[1]+1
count=0
for i in a:
    count+=a[i]
    print(count)

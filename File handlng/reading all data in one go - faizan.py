#program to read all the data
f=open('faizan.txt','r')
st=" "
while st:
    st=f.readline()
    print(st,end=" ")
f.close()

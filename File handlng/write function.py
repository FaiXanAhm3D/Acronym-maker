f=open('write fucntions.txt','w')
for i in range(3):
    name=input("Enter names: ")
    f.write(name)
    f.write('\n') #we cannot write f.write(name,'\n') cuz write() function takes only one arguement
f.close()

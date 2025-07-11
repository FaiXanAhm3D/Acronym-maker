op=open('writelines.txt','w')
lst=[]
for i in range(3):
    a=input("Enter names: ")
    lst.append(a+'\n') #this will send the file pointer to next line
                       #python doesnot write data implicitly by using comma in a list
print(lst)
op.writelines(lst)
#print(op.seek())
op.close()

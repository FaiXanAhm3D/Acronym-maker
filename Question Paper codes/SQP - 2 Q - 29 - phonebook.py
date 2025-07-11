def edit():
    myfile=open('phonebook.dat','r')
    data=myfile.readlines()
    lst=[]
    count=0
    for line in data:
        word=line.split()
        if word[0]=='Arvind':
            word[1]=input("Enter new phone number: ")
            word[1]=word[1]+'\n'
            string=' '.join(word)
            lst.append(string)
            count=1
        else:
            lst.append(line)
    myfile.close()
    if count==0:
        print('Data not found')
    else:
        myfile=open('phonebook.dat','w')
        myfile.writelines(lst)
        myfile.close()

edit()
myfile_data=open('phonebook.dat','r').read()
print(myfile_data)

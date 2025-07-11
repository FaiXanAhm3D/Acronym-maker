import pickle
def CreateFile():
    myfile=open('Myfile.dat','wb')
    data=[]
    while True:
        bookno=int(input("Enter Book No. :"))
        name=input("Enter Book Name: ")
        author=input("Enter author: ")
        price=int(input("Enter price: "))
        data=[bookno,name,author,price]
        pickle.dump(data,myfile)
        myfile.flush()
        cont=input("Add more y/n: ")
        if cont=='n':
            myfile.close()
            break
        else:
            continue

func=input("Insert Data y/n: ")
if func=='y':
    CreateFile()
elif func=='n':
    quit
else:
    print("Wrong Input: ")
    

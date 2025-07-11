import pickle
myfile=open('inventory.dat','wb')
d1=(1, 'ABC', 100, 5000)
d2=(2, 'DEF', 250, 1000)
d3=(3, 'GHI', 300, 2000)
pickle.dump(d1,myfile)
pickle.dump(d2,myfile)
pickle.dump(d3,myfile)
myfile.close()

def expensiveProducts():
    file=open('inventory.dat','rb')
    lst=[]
    count=0
    while True:
        try:
            data=pickle.load(file)
            lst.append(data)

        except EOFError:
            break
    print(lst)
    for i in lst:
        if i[3]>1000:
            count+=1
            print('Product ID:',i[0])
    print('Total expensive products: ',count)
    file.close()
expensiveProducts()

import pickle
myfile=open('student_data.dat','rb')
lst=[]
try:
    while True:
        data=pickle.load(myfile)
        lst.append(data)
except EOFError:
    myfile.close()

for i in lst:
    print(i)

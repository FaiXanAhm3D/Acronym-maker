import pickle
try:
    with open('student_data.dat','rb') as myfile:
        data=pickle.load(myfile)
        for i in data:
            print(i)
except EOFError:
    print('an error occured')

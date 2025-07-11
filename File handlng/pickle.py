import pickle
myfile=open('student_data','wb')
while True:
    roll=input("Enter roll: ")
    name=input("Enter name: ")
    marks=input("Enter marks: ")
    data=roll+':'+':'+name+':'+marks
    pickle.dump(data,myfile)
    cont=input("Add more y/n : ")
    if cont=='n':
        break
    else:
        continue

myfile.close()

#connected with FH 6
with open('marks.txt','a') as myfile:
    for i in range(2):
        roll=int(input("Enter roll: "))
        name=input("Enter name: ")
        marks=int(input("Enter marks: "))
        data=str(roll)+':'+name+':'+str(marks)+'\n'
        myfile.write(data)
print('data inserted successfully')

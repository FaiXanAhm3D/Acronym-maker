count=int(input("Enter the number of student: "))
myfile=open('marks.txt','w')
for i in range(count):
    print("Enter details of student",i+1)
    roll=int(input("Enter the roll : "))
    name=input("Enter the name : ")
    marks=int(input("Enter the marks : "))
    details=str(roll)+':'+name+':'+str(marks)+'\n'
    myfile.write(details)
print("Data inserted succesfully")
myfile.close()

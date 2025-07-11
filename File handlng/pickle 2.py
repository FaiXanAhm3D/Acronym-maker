import faker
fake=faker.Faker()
import pickle
student_dat=[]

while True:
    student={}
    roll=fake.random_number()
    name=fake.name()
    marks=fake.building_number()
    student['roll']=roll
    student['name']=name
    student['marks']=marks
    student_dat.append(student)
    cont=input("Add more y/n : ")
    if cont=='n':
        break
    else:
        continue
with open('student_data.dat','wb') as myfile:
    pickle.dump(student_dat,myfile)

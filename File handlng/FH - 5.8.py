import faker
fake=faker.Faker()
import pickle
emp1={'empno':61279,'name':fake.name(),'age':12,'salary':2000}
emp2={'empno':61280,'name':fake.name(),'age':13,'salary':3000}
emp3={'empno':61281,'name':fake.name(),'age':14,'salary':4000}
emp4={'empno':61282,'name':fake.name(),'age':15,'salary':5000}
lst=[emp1,emp2,emp3,emp4]
myfile=open('emp.dat','wb')
for i in lst:
    pickle.dump(i,myfile)
myfile.close()

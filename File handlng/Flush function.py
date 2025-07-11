import faker
fake=faker.Faker()
n=int(input('Enter number of data: '))
lst=[]
with open('flush.txt','w') as myfile:
    for i in range(n):
        name=fake.name()
        lst.append(name+'\n')
    myfile.writelines(lst)
    myfile.flush()


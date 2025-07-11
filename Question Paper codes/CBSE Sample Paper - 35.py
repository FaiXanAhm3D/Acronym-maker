import random
games=['Cricket','Football','Chess','Basketball','Baseball','Hockey']
results=['won','lose','tie']
import faker
fake=faker.Faker()
import csv
def Accept():
    with open('Result.csv','r+',newline='') as myfile:
        write=csv.writer(myfile)
        read=csv.reader(myfile)
        for i in read:
            if i[0]!='Student ID':
                heading=['Student ID','Student Name','Game Name','Result']
                myfile.seek(0,0)
                write.writerow(heading)
                myfile.seek(0,2)
        
        while True:
            st_id=fake.random_int()
            st_name=fake.name()
            game=random.choice(games)
            result=random.choice(results)
            data=[st_id,st_name,game,result]
            write.writerow(data)
            cont=input("Add more y/n: ")
            if cont=='n':
                break
            else:
                continue
    return True
def wonCount():
    count=0
    lst=[]
    with open('Result.csv','r+') as result:
        result_read=csv.reader(result)
        for i in result_read:
            lst.append(i)
        x=lst.pop(0)
        lst.pop(0)
        for i in lst:
            print(i)
            if i[3].lower()=='won':
                count+=1
            else:
                continue
        print(f'Number of students who have won any event: {count}')
call=Accept()
if call==True:
    wonCount()


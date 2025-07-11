import csv
def ADD():
    myfile=open('record.csv','a',newline='')
    write=csv.writer(myfile)
    while True:
        emp_id=int(input("Enter ID: "))
        emp_name=input("Enter name: ")
        phone=int(input("Enter phone: "))
        salary=int(input("Enter salary: "))
        lst=[emp_id,emp_name,phone,salary]
        write.writerow(lst)
        cont=input("Add more y/n: ")
        if cont=='n':
            myfile.close()
            break
        else:
            continue

def COUNTR():
    myfile=open('record.csv','r',newline='')
    read=csv.reader(myfile)
    data=[]
    for i in read:
        data.append(i)
    data.pop(0)
    print(data)
    print("Total number of records:",len(data))

ADD()
COUNTR()

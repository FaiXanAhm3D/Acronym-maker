def remove():
    st_dat=open('student_data.csv','r+')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    l=[]
    for i in read_data:
        l.append(i)
    x=l.pop(0)
    y=l.pop(0)
    del_data=int(input("Enter the roll of the user you want to delete: "))
    for i in l:
        if i[0]==del_data:
            l.pop(i)
            break
    st_dat.seek(0,0)
    write_data.writerow(x)
    write_data.writerow(y)
    write_data.writerows(l)
    st_dat.close()

def search():
    st_dat=open('student_data.csv','r+')
    read_data=csv.reader(st_dat)
    c=0
    search_roll=input("Enter Roll number of the student: ")
    for i in read_data:
        if search_roll==i[0]:
            print(i)
            c+=1
            break
    if c==0:
        print('Student with roll no.',search_roll,'not found',)
        print(' ')
    st_dat.close()

def sort():
    st_dat=open('student_data.csv','r+',newline='')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    l=[]
    for i in read_data:
        l.append(i)
    x=l.pop(0)
    y=l.pop(0)
    for i in l:
        i[0]=int(i[0])
    l.sort()
    st_dat.seek(0,0)
    write_data.writerow(x)
    write_data.writerow(y)
    write_data.writerows(l)
    print("Data sorted",end='\n')
    st_dat.close()

def show():
    st_dat=open('student_data.csv','r+',newline='')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    show_lst=[]
    for ch in read_data:
        show_lst.append(ch)
    x=show_lst.pop(0)
    y=show_lst.pop(0)
    for s in show_lst:
        print(s)
    st_dat.seek(0,0)
    write_data.writerow(x)
    write_data.writerow(y)
    write_data.writerows(show_lst)
    print(' ')
    st_dat.close()

def add(): #edit this function...
    dup=open('student_data.csv','r+',newline='')
    k='yes'
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    l=[]
    for i in read_data:
        l.append(i)
    x=l.pop(0)
    y=l.pop(0)
    while k.lower().strip()=='yes':
        count=0
        name=input("Enter name of student: ")            
        roll=input("Enter roll of student: ")
        phy_marks=input("Enter marks of Physics ==> ")
        chem_marks=input("Enter marks of Chemistry ==> ")
        math_marks=input("Enter marks of Maths ==> ")
        dup_roll=csv.reader(st_dat)
        temp_data=[roll,name,phy_marks,chem_marks,math_marks]
        if temp_lst!=[]:
            for ch in temp_lst:
                if ch[0]==roll:
                    print("Roll number already exists")
                    print("Try again")
                    temp_lst.pop(ch)
                    count+=1
                    break
        else:
            temp_lst.append(temp_data)
        lst=[]
        for i in dup_roll:
            lst.append(i)
        for j in lst:
            if roll in j:
                print("DATA ALREADY EXIST-->",j)
                print("Do you want to 'APPEND' or 'OVERWRITE'?",end=" ")
                function=input("Enter your choice: ")
                if function.lower().strip()=='overwrite':
                    overwrite_dat=open('student_data.csv','w',newline='')
                    write_dat=csv.writer(st_dat)
                    pos=lst.index(j)
                    lst.pop(pos)
                    lst.insert(pos,[roll,name,phy_marks,chem_marks,math_marks])
                    write_dat.writerows(lst)
                    count+=1
                    print('>>>Data overwriten successfully<<<')
                    break
                elif function.lower().strip()=='append':
                    continue
        if count==1:
            k=input("Do you want to add more ?'\n'Yes or No ==> ")
            if k.lower().strip()=='no':
                break
        elif count==2:
            k='yes'
        elif count==0:
            k=input("Do you want to add?'\n'Yes or No ==> ")
            if k.lower().strip()=='yes':
                write_data.writerow([roll,name,phy_marks,chem_marks,math_marks])
            elif k.lower().strip()=='no':
                write_data.writerow([roll,name,phy_marks,chem_marks,math_marks])
                print(">>>DATA INSERTED SUCCESSFULLY<<<")
                break
            else:
                temp_lst.pop()
                k='yes'
                print(">>>           INVALID INPUT          <<<")
                print(">>>      DATA INSERTION FAILED       <<<")
                print(">>>            TRY AGAIN             <<<")
                print(">>>       RE-TRY FOR LAST DATA       <<<")
        else:
            break
    dup.close()

temp_lst=[]

import csv
st_dat=open('student_data.csv','a+',newline='')
write_data=csv.writer(st_dat)
read_data=csv.reader(st_dat)
st_dat.seek(0,0)
read1=st_dat.read(1)
if read1!='R':
    write_data.writerow(['Roll No.','Name of student',"",'Subject'])
    write_data.writerow(["","",'PHYSICS','CHEMISTRY','MATHS'])
st_dat.seek(0,0)

while True:
    function=input("Enter 'SHOW' to show data\nEnter 'ADD' to add data\nEnter 'SORT' to sort data\nEnter 'SEARCH' to search data\nEnter 'QUIT' to end the programme\nEnter the function --->")
    print(' ')
    if function.lower().strip()=='show':
        show()
    elif function.lower().strip()=='add':
        add()
    elif function.lower().strip()=='sort':
        sort()      o
    elif function.lower().strip()=='search':
        search()
    elif function.lower().strip()=='remove':
        remove()
    elif function.lower().strip()=='quit':
        print(">>>End Of Programme<<<")
        st_dat.close()
        break
    else:
        print(">>>Invalid Input<<<")
        print(' ')

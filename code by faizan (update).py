def add(): #edit this function...
    st_dat=open('student_data.csv','r+',newline='')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    k='yes'
    while k.lower().strip()=='yes':
        name=input("Enter name of student: ")
        roll=input("Enter roll of student: ")
        check=check_roll(roll)
        if check=='y':
            print("DATA ALREADY EXIST-->",c)
                print("Do you want to 'APPEND' or 'OVERWRITE'?",end=" ")
                function=input("Enter your choice: ")
                if function.lower().strip()=='overwrite':
                    overwrite()

def check_roll(roll):
    st_dat=open('student_data.csv','r+',newline='')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    l=[]
    for i in read_data:
        l.append(i)
    x=l.pop(0)
    y=l.pop(0)
    for ch in l:
            if ch[0]==roll:
                global c
                c=ch
                return 'y'
    st_dat.close()
def overwrite():
    st_dat=open('student_data.csv','r+',newline='')
    read_data=csv.reader(st_dat)
    write_data=csv.writer(st_dat)
    l=[]
    for i in read_data:
        l.append(i)
    x=l.pop(0)
    y=l.pop(0)
    
            
            
        

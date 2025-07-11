import csv
st_dat=open('student_data.txt','a+')
read_data=csv.writer(st_dat)
st_dat.seek(0,0)
read1=st_dat.read(1)
k='yes'
if read1!='R':
    read_data.writerow(['Roll No.','%25s'%'Name of student','%45s'%'Subject'])
    read_data.writerow(['%65s'%'PHYSICS','%15s'%'CHEMISTRY','%10s'%'MATHS'])
    read_data.writerow(['============================================================================================'])
while k.lower()=='yes':
    name=input("Enter name of student: ")
    roll=input("Enter roll of student: ")
    phy_marks=input("Enter marks of Physics ==> ")
    chem_marks=input("Enter marks of Chemistry ==> ")
    math_marks=input("Enter marks of Maths ==> ")
    read_data.writerow([roll,'%30s'%name,'%27s'%phy_marks,'%15s'%chem_marks,'%13s'%math_marks])
    k=input("Do you want to continue?'\n'Yes or No ==> ")
    if k.lower()=='no':
        break
    elif k.lower()!='no' and k.lower()!='yes':
        print("Invalid input")
        continue
st_dat.close()
    
        
    

mydict={}
num=int(input("Enter number of employees: "))
while num>0:
    name=input("Enter the name of the employee: ")
    salary=int(input("Enter the salary of the respective employee: "))
    mydict[name]=salary
    num-=1
    
print(mydict)

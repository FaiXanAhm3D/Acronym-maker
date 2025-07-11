a=int(input("Enter the number of employees: "))
Dict={}
while a>0:
    name=input("Enter name of employee: ")
    salary=int(input("Enter the salary of the employee: "))
    Dict[name]=salary
    a-=1
print(Dict)
    

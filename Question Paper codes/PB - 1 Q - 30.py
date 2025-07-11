def push_projects(proj_stk,emp_dict):
    keys=emp_dict.keys()
    for i in keys:
        if emp_dict[i]==(True,True,True):
            proj_stk.append(i)
    #print(proj_stk)

def pop_projects(proj_stk):
    length=len(proj_stk)
    while True:
        if proj_stk != []:
            print(proj_stk.pop())
        else:
            print('Stack empty')
            break
emp_dict={101:(True,True,True),102:(False,True,True),103:(True,True,False),104:(True,True,True),105:(False,False,False)}
proj_stk=[]
push_projects(proj_stk,emp_dict)
pop_projects(proj_stk) 

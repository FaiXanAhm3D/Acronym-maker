def Push_elements(Nlist):
    lst=[]
    for i in Nlist:
        if i[1]!='India' and i[2]<3500:
            element=[i[0],i[1]]
            lst.append(element)
    return lst
def Pop_element():
    length=len(lst)
    while True:
        if lst==[]:
            print('Stack Empty')
            break
        else:
            print(lst.pop())

Nlist=[['New York','USA',11734],['Naypyidaw','Myanman',3219],['Dubai','UAE',2194],['London','England',6693],['Gangtok','India',1580],['Columbo','Sri Lanka',3405]]
lst=Push_elements(Nlist)
Pop_element()

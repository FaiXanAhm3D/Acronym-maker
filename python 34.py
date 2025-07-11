def SQUARE_LIST(L):
    lst=[]
    for i in L:
        if i!=0:
            element=i**2
            lst.append(element)
        elif i==0:
            continue
    return lst
user_list=[]
number=int(input("Enter number of elements: "))
for i in range(number):
    element=int(input("Enter the element: "))
    user_list.append(element)
SList=SQUARE_LIST(user_list)
print(SList)

        
        
        

def INDEX_LIST(L):
    lst=[]
    for i in L:
        if i!=0:
            lst.append(L.index(i))
        elif i==0:
            continue
    return lst
user_lst=[]
number_of_element=int(input("Enter the number of elements: "))
for i in range(number_of_element):
    element=int(input("Enter the element: "))
    user_lst.append(element)
indexList=INDEX_LIST(user_lst)
print("Index of all the non-zero elements are",indexList)
            

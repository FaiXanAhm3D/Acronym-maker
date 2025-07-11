def modifylist(L,n):
    for i in L:
        if i%n==0:
            i+=5
        else:
            i-=5
    return L
a=int(input("Enter number of elements: "))
lst=[]
for i in range(a):
    value=int(input("Enter the element: "))
    lst.append(value)
x=int(input("Enter a divisor: "))
mod_list = modifylist(lst,x)
print(mod_list)

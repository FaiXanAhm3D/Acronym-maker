#program to input list of numbers and swap elements at the even location with elements at the odd location

def swap(lst):
    length=len(lst)
    for i in range(0,length-1,2):
        lst[i],lst[i+1]=lst[i+1],lst[i]
    print(lst)

lst=[]
while True:
    a=int(input("Enter a number: "))
    lst.append(a)
    cont=input("Add more y/n: ")
    if cont=='n':
        break
    else:
        continue
swap(lst)
        

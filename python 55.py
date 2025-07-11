#function that accepts a list of numbers as arguement and increases the value of the elements-
#by 10 if the elemts are divisible by 5 

def modilist(L):
    lst=[]
    for i in L:
        if i%5==0:
            i+=10
            lst.append(i)
        else:
            lst.append(i)
    return lst
num=[]
while True:
    a=int(input("Enter a number: "))
    num.append(a)
    cont=input("Add more y/n : ")
    if cont=='n':
        break
    else:
        continue
mod=modilist(num)
print(mod)

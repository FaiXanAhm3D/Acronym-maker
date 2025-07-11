def Swapper(numbers):
    index=len(numbers)//2
    numbers=numbers[index:]+numbers[:index]

    print(numbers)
    
    

length=int(input("Enter length of the list (even only): "))
lst=[]
for i in range(length):
    num=int(input("Enter number: "))
    lst.append(num)
    
Swapper(lst)

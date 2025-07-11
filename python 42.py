def marks(lst):
    total=0
    length=len(lst)
    max_marks=max(lst)
    min_marks=min(lst)
    for i in lst:
        total+=i
    avg_marks=total/length
    print(f"maximum marks = {max_marks}")
    print(f"minimum marks = {min_marks}")
    print(f"average marks = {avg_marks}")
lst=[]
while True:
    num=int(input("Enter marks: "))
    cont=input("Add more y/n: ")
    lst.append(num)
    if cont=='y':
        continue
    elif cont=='n':
        break
marks(lst)

    

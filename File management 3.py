with open('notes.txt','r') as file:
    data = file.read()
    data=data.split()
    count=0
    for i in data:
        if i=='IS' or i=='TO' or i=='UP':
            count+=1
    print(count)



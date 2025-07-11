lst=[]
with open('faizan.txt','r') as myfile:
    data=myfile.read()
    data=data.split()
    for i in data:
        for j in i:
            if j.isdigit()==True:
                print(j)


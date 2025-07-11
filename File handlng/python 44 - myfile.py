with open('myfile.txt','r') as file:
    data=file.readlines()
    line_a=[]
    line_b=[]
    for i in data:
        if 'a' in i:
            data.remove(i)
            line_a.append(i)     
with open("myfile_a.txt",'w') as file_a:
    file_a.writelines(line_a)
with open("myfile.txt",'w') as file_b:
    file_b.writelines(data)
    

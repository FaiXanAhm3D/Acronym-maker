import csv
myfile=open('FLIGHT.csv','r')
read=csv.reader(myfile)
for i in read:
    print(i)

def delete_row(read):
    myfile_row=open('FLIGHT.csv','w')
    write=csv.writer(myfile_row)
    lst=[]
    for i in read:
        lst.append(i)
    lst.pop(-1)
    write.writerows(lst)
    
    

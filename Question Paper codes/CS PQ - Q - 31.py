import csv
def maxsalary():
    myfile=open('record.csv','r')
    read=csv.reader(myfile)
    lst=[]
    for i in read:
        lst.append(i)
    x=lst.pop(0)
    for i in lst:
        i[3]=int(i[3])
    lst.sort()
    print(lst[0])

maxsalary()


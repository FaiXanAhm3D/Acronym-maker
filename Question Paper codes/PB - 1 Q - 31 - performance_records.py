import csv
def highest_performer():
    with open('performance_records.csv','r') as myfile:
        read=csv.reader(myfile)
        #write=csv.writer(myfile)
        lst=[]
        for i in read:
            lst.append(i)
        #print(lst)
        x=lst.pop(0)
        #print(lst)
        for i in lst:
            i[4]=float(i[4])
        lst.sort()
        print(lst[-1])

highest_performer()

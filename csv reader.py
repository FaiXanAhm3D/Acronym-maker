import csv
with open('next.csv','r') as file:
    read=csv.reader(file)
    for i in read:
        print(i,end=' ' )

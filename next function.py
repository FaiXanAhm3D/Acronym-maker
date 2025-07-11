#next() function
import csv
with open('next.csv','r+') as file:
    reader=csv.reader(file)
    first=next(reader) #here the next() function will skip the first row
    print(first) # this will print the first line(or row)
    for i in reader:
        print(i)

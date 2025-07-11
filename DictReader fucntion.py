#use of dictreader function

import csv
with open('next.csv','r+') as file:
    reader=csv.DictReader(file) #this reader fucntion will return the data in dictionary format
    for i in reader:            #the heading of each column is the key
        print(i['marks']) 
        

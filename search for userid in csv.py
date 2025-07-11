import csv
userid=input("Enter the userid: ")
with open('myfile.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['userid']==userid:
            print(row['password'])

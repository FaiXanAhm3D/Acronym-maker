with open('myfile.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rate = int(row['rate'])
        if 500 <= rate <= 1000:
            print(row)

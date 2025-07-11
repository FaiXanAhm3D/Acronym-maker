def count():
    with open('gratitude.txt','r') as myfile:
        data=myfile.readlines()
        line_count=0
        for line in data:
            line_count+=1
            e_count=0
            words=line.split()
            for word in words:
                if word[-1]=='e':
                    e_count+=1
            print(f'line {line_count} : {e_count}')

count()

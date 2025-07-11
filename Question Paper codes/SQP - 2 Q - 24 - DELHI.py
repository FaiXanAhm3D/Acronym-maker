def start():
    with open('DELHI.txt','r') as myfile:
        data=myfile.readlines()
        for i in data:
            if i[0]=='D' or i[0]=='M':
                print(i)
            else:
                continue
start()

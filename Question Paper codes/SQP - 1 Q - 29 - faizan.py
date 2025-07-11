def count_words():
    with open('faizan.txt','r') as myfile:
        data=myfile.read()
        data=data.split()
        n=len(data)
    print(n)
count_words()

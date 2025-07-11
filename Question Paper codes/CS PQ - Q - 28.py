'''Write a function COUNT() in Python to read from a text file'Gratitude.txt' and
display the count of the letter 'e' in eachline'''

def COUNT():
    myfile=open('gratitude.txt','r')
    data=myfile.readlines()
    line_count=0
    for line in data:
        line_count+=1
        words=line.split()
        e_count=0
        for word in words:
            for letter in word:
                if letter.lower()=='e':
                    e_count+=1
                else:
                    continue
        print(f"line {line_count} : {e_count}")
    
COUNT()

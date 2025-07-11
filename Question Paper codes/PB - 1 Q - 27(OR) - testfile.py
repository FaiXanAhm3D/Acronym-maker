def VOWEL_WORDS():
    with open('testfile.txt','r') as myfile:
        data=myfile.read()
        #print(data)
        words=data.split()
        a_count=0
        u_count=0
        for i in words:
            if i[0].lower()=='a':
                a_count+=1
            elif i[0].lower()=='u':
                u_count+=1
        print(f"The number of words starting with letter 'a' is : {a_count}")
        print(f"The number of words starting with letter 'u' is : {u_count}")

VOWEL_WORDS()




with open("heshecount.txt",'r') as file:
    data=file.read()
    word=data.split()
    he_count=0
    she_count=0
    for i in word:
        if i=='He':
            he_count+=1
        if i=='She':
            she_count+=1
    print(f"Frequency of 'He' = {he_count}")
    print(f"Frequency of 'She' = {she_count}")

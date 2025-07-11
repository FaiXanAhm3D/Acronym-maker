with open('myfile.txt','r') as file:
    uppercase=0
    lowercase=0
    vowel=0
    consonants=0
    data = file.read()
    for i in data:
        if i.isupper():
            uppercase+=1
        if i.islower():
            lowercase+=1
        if i in ['a','e','i','o','u']:
            vowel+=1
        else:
            consonants+=1
    print(f"Number of vowel = {vowel}")
    print(f"Number of consonants = {consonants}")
    print(f"Number of uppercase characters = {uppercase}")
    print(f"Number of lowercase characters = {lowercase}")


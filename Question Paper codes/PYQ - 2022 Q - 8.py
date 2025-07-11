def PushNV(N):
    NoVowel=[]
    vowel=['a','e','i','o','u']
    for i in N:
        count=0
        for j in vowel:
            if j in i.lower():
                count+=1
            else:
                continue
        if count==0:
            NoVowel.append(i)
        else:
            continue
    return NoVowel

i=1
ALL=[]
while i<=5:
    item=input("Enter a word: ")
    ALL.append(item)
    i+=1
result=PushNV(ALL)

while True:
    if result==[]:
        print("EmptyStack")
        break
    else:
        print(result.pop())
    

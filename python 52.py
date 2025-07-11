def PushNV(N):
    lst=[]
    for i in N:
        if 'a' not in i and 'e' not in i and 'i' not in i and 'o' not in i and 'u' not in i:
                lst.append(i)
    return lst

ALL=[]
for i in range(5):
    a=input("Enter a word: ")
    ALL.append(a)
print(f"List of all the words: {ALL}")
result=PushNV(ALL)
print(f"String with no vowels: {result}")

for i in range(len(result)):
    b=result.pop()
    print(b,end=" ")
    if result==[]:
        print("EmptyStack")

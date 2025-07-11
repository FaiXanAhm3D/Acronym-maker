#function which accepts a string and print each individual word of it along with its length

def wordlength():
    a=input("Enter a statement: ")
    lst=a.split()
    for i in lst:
        length=len(i)
        print(f"{i} ({length})")
wordlength()

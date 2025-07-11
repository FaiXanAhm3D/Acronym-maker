def FindWord(string,search):
    lst=string.split()
    count=0
    for i in lst:
        if i.lower()==search.lower():
            count+=1
    print(f"{search} occured {count} times in entered string")

string=input("Enter a string: ")
search=input("Enter word to search: ")
FindWord(string,search)

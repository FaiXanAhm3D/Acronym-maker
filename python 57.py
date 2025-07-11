#function to read content of a text file and display the entire content in captial letters

def capit():
    with open("notes.txt",'r') as file:
        data=file.read()
        for i in data:
            print(i.upper(),end="")
capit()

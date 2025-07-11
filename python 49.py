book_titles=['ncert','oswal','harry potter']
def PushOn(book):
    for i in book:
        book_titles.append(i)
    print(book_titles)
def Pop(book):
    for i in range(len(book)):
        book_titles.pop()
    print(book_titles)

print('''Enter 1 to insert
Enter 2 to delete''')
function=int(input("Enter function: "))
if function == 1:
    push_book=[]
    while True:
        push_name=input("Enter the name to insert: ")
        push_book.append(push_name)
        cont=input("Add more y/n: ")
        if cont=='n':
            break
        else:
            continue
    PushOn(push_book)
if function==2:
    pop_book=[]
    while True:
        pop_name=input("Enter the name to delete: ")
        pop_book.append(pop_name)
        cont=input("Add more y/n: ")
        if cont=='n':
            break
        else:
            continue
    Pop(pop_book)

def dispBook(BOOKS):
    lst=[]
    vowel=['a','e','i','o','u']
    for i in BOOKS:
        count=0
        book=BOOKS[i].lower()
        for j in vowel:
            if j == book[0]:
                count+=1
            else:
                continue
        if count==0:
            print(book.upper())
        else:
            continue
BOOKS = {1:"Python", 2:"Internet Fundamentals ", 3:"Networking ",4:"Oracle sets", 5:"Understanding HTML"}
dispBook(BOOKS)

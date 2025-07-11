user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = ""
for i in text:
    a = a+str(i[0]).upper() #here it is capitalising the first letter of very word and concatinating it into one
print(a)

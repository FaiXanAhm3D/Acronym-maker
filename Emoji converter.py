msg=input(">>>")
words=msg.split(' ')
emoji={
    ":)" : "☺",
    ":(" : "☹️",
    "XD" :
    ":'')" : ""
}
output=""
for word in words:
    output += emoji.get(word,word) + " "
print(output)
    

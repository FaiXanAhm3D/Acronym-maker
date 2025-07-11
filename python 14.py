str01="abcd 1234 faizan India !@#"
d=0
u=0
l=0
w=0
for i in str01:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
    if i.isdigit():
        d+=1
    if i==" ":
        w+=1
print("upper = ",u)
print("lower = ",l)
print("digit = ",d)
print("space = ",w)

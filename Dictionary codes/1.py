dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "colour":["red","white","blue"],
    "abcd":"Mustang",
    "pqe":1964,
    "home":"Ford"
    }
lst_key=[]
for i in dictionary:
    lst_key.append(i)
#print(lst_key)
lst_value=[]
for i in dictionary:
    lst_value.append(dictionary[i])
#print(lst_value)
#for i in lst_key:
    #print(dictionary[i])

for i in lst_key:
    for j in lst_value:
        if dictionary[i] is dictionary[j]:
            del dictionary[i]
print(dictionary)
    



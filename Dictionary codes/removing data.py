dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "colour":["red","white","blue"]
    }
x=dictionary.pop('colour')
print(x)
print(dictionary)

#or

y=dictionary.popitem()
print(y)
print(dictionary)

#The popitem() method removes the last inserted item

#or

del dictionary['model']
print(dictionary)

#The del keyword removes the item with the specified key name
#The del keyword can also delete the dictionary completely
del dictionary

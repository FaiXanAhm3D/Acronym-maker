dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "colour":["red","white","blue"]
    }

x=dictionary.items()
print(x)

#The items() method will return each item in a dictionary, as tuples in a list.
for i in dictionary:
    print(i)

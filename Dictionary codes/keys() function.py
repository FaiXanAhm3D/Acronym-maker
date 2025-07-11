dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
    }

x=dictionary.keys()
print(x) #before

dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
    }
dictionary["colour"]='red'
x=dictionary.keys()
print(x) #after

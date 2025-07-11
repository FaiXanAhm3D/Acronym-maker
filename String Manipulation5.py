name = input("Enter your name: ")

if len(name) < 4:
    print("Name must be at least 4 charachters")

elif len(name) > 20:
         print("Name must be a maximum of 20 charachters")

else:
    print("Name looks good i.e " + name)



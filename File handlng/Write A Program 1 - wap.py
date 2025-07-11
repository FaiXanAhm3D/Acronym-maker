with open('wap.txt','w') as p:
    while True:
        name=input("Enter name: ")
        p.write(name+'\n')
        cont=input("Do you want to add more ?\n Yes or No--> ")
        if cont.lower()=='no':
            break
        elif cont.lower()!='no' and cont.lower()!='yes':
            print('Invalid input')
            break
print('End Of Program')

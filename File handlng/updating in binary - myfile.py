import pickle
roll=input("Enter the roll: ")
marks=input("Enter the updated marks: ")
with open('myfile.dat','ab') as file:
    try:
        while True:
            data=pickle.load(file)
            if roll in data:
                data[2]=marks

    except EOFError:
        print("Roll number not found")
        break
        

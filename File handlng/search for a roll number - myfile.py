import pickle

roll = input("Search roll number: ")
with open('myfile.dat', 'rb') as file:
    while True:
        try:
            data = pickle.load(file)
            if data[1] == roll:
                print(data[0])
                break
        except EOFError:
            print("Roll number not found")
            break

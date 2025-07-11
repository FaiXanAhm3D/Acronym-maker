import pickle

def read():
   with open("data.dat", "rb") as f:
       while True:
            try:
                d = pickle.load(f)
                if d['age'] == 16:
                    print(d)
            except EOFError:
                break

read()

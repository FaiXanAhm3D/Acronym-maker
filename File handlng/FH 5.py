import pickle
with open('myfile.dat','rb') as file:
    lst=['faizan','kv kankinara',12]
    pickle.dump(lst,file)
    data=pickle.load(file)
    print(data)
    

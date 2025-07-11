import pickle
a=open('faizan.txt','rb')
s=pickle.load(a)
print(s)
a.close()

def insert():
    d1={'rollno':1001,'name':'tom','age':17}
    d2={'rollno':1002,'name':'bob','age':16}
    d3={'rollno':1003,'name':'kay','age':16}
    file=open("data.dat",'w')
    pickle.dump(d1,file)
    pickle.dump(d2,file)
    pickle.dump(d3,file)
    f.close()
insert()
    

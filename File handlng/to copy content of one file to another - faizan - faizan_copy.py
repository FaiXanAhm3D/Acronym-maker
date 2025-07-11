with open('faizan.txt','r') as f:
    r=f.readlines()

c=open('faizan_copy.txt','w')
c.writelines(r)
c.close()
print("DONE")

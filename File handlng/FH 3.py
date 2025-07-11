file=open('FH3.txt','w')
lst=['Physics\n','Chemistry\n','Math\n']
file.writelines(lst)
file.close()
print("DONE")

with open('FH3-1.txt','w') as f:
    lit=['English','Hindi','Chemistry']
    f.writelines(lit)
    print('is file closed?-->',f.closed)

print('Is file closed?-->',f.closed)

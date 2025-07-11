file=open('FHT.txt','w')
lst=['Physics\n','Chemistry\n','Math\n']
file.writeline(lst) #what would happen if we will use writeline() instead of writelines()
file.close()
print("DONE")

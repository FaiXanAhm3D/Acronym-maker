#read function

f=open('faizan.txt','r')
read=f.read(5)
read2=f.read(10)
print(read,end='')
print(read2)
#print(len(read2))

f.seek(0,0)

line=f.readline(15) #read one line at a time in the form of string
#if n is specified reads at most n bytes
print(line)
#print(len(line))
lines=f.readlines() #read the entire data in one go in the form of list
print(lines)

f.seek(0,0)

file=open('faizan.txt','r').read() #nested program
#print(len(file))
print(file)
f.close()

def runMe(x=1, y=2):
    x = x+y
    y+=1
    print(x, '$', y)
    return x,y
a,b = 2, 1
a,b = runMe()
print(a, '#', b)
runMe(a,b)

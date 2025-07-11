data=["L",20,"M",40,"N",60]
times=0
alpha=""
add=0
for c in range(1,6,2):
    times = times + c
    alpha = alpha + data [c-1] + "@"
    add = add + data[c]
    print (times, add, alpha)

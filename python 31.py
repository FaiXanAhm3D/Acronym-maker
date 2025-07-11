def func(Data=["A",0,"B",0,"C",0]):
    Times = 0
    Alpha = ""
    Add = 0
    for C in range(1,6,2):
        Times= Times + C
        Alpha= Alpha + Data[C-1]+"$"
        Add = Add + Data[C]
    return Times, Add, Alpha
x = ["P",20,"R",10,"S",30]
y = func(x)
print(y[0], y[1], y[2])

def changer(p,q=10):
    p=p/q
    q=p%q
    print(p,'#',q)
    return p
a=200
b=20
a=changer(a,b)
print(a,'$',b)
b=changer(b)
print(a,'$',b)
a=changer(a)
print(a,'$',b)

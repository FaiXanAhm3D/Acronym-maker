import itertools
a=[1,2]
b=[3,4]
prod=itertools.product(a,b)
print(prod)
print(list(prod))

prod=itertools.product(a,b,repeat=2)
print(prod)
print(list(prod))

a=[1,2,3]
perm=itertools.permutations(a)
print(perm)
print(list(perm))

a=[1,2,3]
perm=itertools.permutations(a,2) #length of permutation
print(perm)
print(list(perm))

a=[1,2,3,4]
comb=itertools.combinations(a,2)
print(comb)
print(list(comb))

a=[1,2,3,4]
acc=itertools.accumulate(a)
print(acc)
print(a)
print(list(acc))







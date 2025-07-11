#sets
myset={1,2,3,4,5,'a','b','c','d'}
yourset={'a','b','c'}
myset.add('e')
print(myset)
#myset.clear() output --> set()

print(yourset.union(myset))
print(yourset.issubset(myset))
print(myset.difference(yourset))
print(myset.symmetric_difference(yourset))
print(yourset.update(myset))


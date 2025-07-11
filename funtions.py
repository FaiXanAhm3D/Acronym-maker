#Funtions
#in built funtion
int()
str()
bool()
#module funtion
import math
print(dir(math))

from math import sqrt
print(sqrt(9))

from math import*
print(sqrt(25))

#user defined funtion
def print_sum(first,second=5):
    print(first+second)

print_sum(1,)



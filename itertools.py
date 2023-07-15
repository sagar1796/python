# iterators tools is collection of tools for handling the iterators
#itertools : products, permuation, combination, groupby and infinite iterators
from itertools import product
a=[3,3]
b=[2,1]
prod=product(a,b)
print(prod)
print(list(prod))
prod=product(a,b,repeat=2)
print(list(prod))
#permutation
from itertools import permutations
a=[1,2,3]
print(list(permutations(a)))
print(list(permutations(a,2)))

#combination
from itertools import combinations,combinations_with_replacement
a=[1,2,3,4]
print(list(combinations(a,2)))

print(list(combinations_with_replacement(a,2)))

#accumalate add the items
from itertools import accumulate
a=[1,2,5,3,4]
acc=accumulate(a)
print(list(acc))
import operator # use the mult or max and accumulate or any other function it
a=[1,2,3,4]
acc=accumulate(a,func=max)
print(list(acc))
#groupby function
from itertools import groupby
def smaller_than_3(x):
    return x<3
a=[1,2,3,4]
group=groupby(a,key=smaller_than_3)  # or use group=groupby(a,key=lambda x:x<3)

print(group)

for key, value in group:
    print(key,list(value))

#infinite iterators
from itertools import count , cycle, repeat
for i in count(10):
    print(i)
    if i==15:
        break

from itertools import  cycle, repeat
a=[1,2,3]
for i in cycle(a):
    print(i)
    if i==2:
        break

from itertools import repeat

for i in repeat(1,4):
    print(i)


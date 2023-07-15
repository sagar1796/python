#lambda arguments : expression
#create a function
add10=lambda x:x+10
print(add10(5))

def add10_fun(a):
    return a+10


mult=lambda x,y:x*y
print(mult(2,3))

point2d=[(1,2),(14,1),(4,-1)]

point2d_sorted=sorted(point2d)
point2d_sorted_y=sorted(point2d,key=lambda x:x[1])
point2d_sorted_sum=sorted(point2d,key=lambda x:x[0]+x[1])

print(point2d)
print(point2d_sorted)
print(point2d_sorted_y)
print(point2d_sorted_sum)

#map(fun,seq)
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

#we can use list ccomphension
c=[x*2 for x in a]
print(c)

#filter function
#filt(func,seq)
a=[1,2,3,4,5]
b=filter(lambda x:x%2==0,a)
print(list(b))

#we can acheive the same using list comphresion
a=[1,2,3,4,5]
b=[i for i in a if i%2==0]
print(b)

#reduce(func,seq)
from functools import reduce
a=[1,2,3,4,5]
product_a=reduce(lambda x,y:x*y,a)
print(product_a)




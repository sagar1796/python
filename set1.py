#sets : unordered, mutable, no duplicates
#create set
my_set={1,2,3,3,2}

print(my_set)

#method2
myset=set([1,2,3,4,2,3])
print(myset)
word=set("hello")
print(word) # good way to know how many character in a document
#empty set
empty=set()
empty.add(1)
empty.add(2)
empty.add(3)
#remove items
empty.remove(3)
#empty.remove(4) # throw an error
#empty.discard(4) # not throw any erro
# clear method
#empty.clear() # clear our set
#empty.pop() # remove one item of our set

#iterations using loooing
for i in my_set:
    print(i)

#item in the set
if 1 in my_set:
    print("yes")

#union and intersection
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print(u)

i=odds.intersection(primes)
print(i)

#difference between two sets
setA={1,2,3,4,5,6,7,8}
setB={1,2,3,10,12}
diff=setA.difference(setB)
print(diff)

#symmentric difference
setA={1,2,3,4,5,6,7,8}
setB={1,2,3,10,12}
diff=setA.symmetric_difference(setB)
print(diff) # {4, 5, 6, 7, 8, 10, 12}

#update
setA={1,2,3,4,5,6,7,8}
setB={1,2,3,10,12}
Set=setA.update(setB)
print(Set) #OUTPUT {1,2,3,4,5,6,7,8,10,12}

#intersection upate
setA={1,2,3,4,5,6,7,8}
setB={1,2,3,10,12}
Set=setA.intersection_update(setB)
print(Set) # out {1,2,3}

# differnce update method
print(setA.difference_update(setB)) #output {4,5,6,7,8}

#symmetric difference update
print(setA.symmetric_difference_update(setB)) # {4, 5, 6, 7, 8, 10, 12}

#subset
print(setA.issubset(setB)) # False or 

print(setB.issubset(setA)) # True or flase

#superset
print(setA.issuperset(setB)) 

#disjoint
print(set=setA.isdisjoint(setB))

#copy set

setC=setB.copy()
#method2
setc=set(setB)

#frozen set 
a=frozenset([1,2,3,4])
a.add(5)
a.remove(2)

print(a) # will get an error

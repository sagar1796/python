#collection: counter data type, nametuple , OrderDict, defaultdict, deque
from collections import Counter

a="aaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccc"
my_count=Counter(a)
print(my_count)
print(my_count.keys())
print(my_count.values())
print(my_count.most_common(1))
print(my_count.most_common(1)[0])
print(my_count.most_common(1)[0][0])

print(set(my_count.elements()))

from collections import namedtuple
point=namedtuple("Point","x,y")
pt1=point(2,4)
print(pt1)
print(pt1.x,pt1.y)

#OrderedDict
from collections import OrderedDict
orderdict=OrderedDict()
orderdict["a"]="kha"
orderdict["b"]="ba"
print(orderdict)

#defaultDict
from collections import defaultdict
d=defaultdict(int)
d["a"]=1
d["b"]=2
print(d)

#deque
from collections import deque
d=deque()
d.append(1)
d.append(1)
d.appendleft(3)
d.pop()
d.popleft()
#d.clear() #remove all the element
#extent the deque
d.extend([4,5,6])
d.extendleft[0]

#rotate the one place
d.rotate(1)


print(d)








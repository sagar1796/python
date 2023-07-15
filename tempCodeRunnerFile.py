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
fruits=["bananas","cheery","apple"]
print(fruits)

#
fruit=fruits[1]
print(fruit)

if "bananas" in fruits:
    print("yes")

else:
    print("no")

#append method 
fruits.append("lemon")

#insert method to specific position
fruits.insert(1,"grapes")
print(fruits)

#delete the items in a list
#pop() method will del last item
item=fruits.pop()
print(item)
#del the specific element in the list
item=fruits.remove("grapes")
print(fruits)

#reverse your list
item=fruits.reverse()
print(fruits)

#sorted method
numbers=[1,3,4,62,12]
sorted_no=numbers.sort()
new_list=sorted(numbers)
print(numbers)
print(new_list)

#slicing list
print(fruits)
fruit1=fruits[0:2]
print(fruits[1:]) # if we don't speicify the last index, it will print all from the start index
print(fruits[:3])# if you don't specify start index go to index 2
print(fruits[::2]) # skip one 2 step at a time
print(fruits[::-1])#reverse our list

print(fruit1)
#copying the list
fruit_copy1=fruits.copy()
fruit_copy=fruits[:]
fruit_copy2=list(fruits)

print(fruit_copy,fruit_copy1,fruit_copy2)

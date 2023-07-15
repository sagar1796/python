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
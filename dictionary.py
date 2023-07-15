#dictionary : key-values pairs,mutable,unordered
#method of creating dictionary
my_dict={"name":"sagar","last_name":"singh","age":30}
print(my_dict)
#method2
details=dict(name="sagar",last_name="singh",age=40)
print(details)

#access the value of the keys
print(my_dict["name"])
print(my_dict["last_name"])

# add the key and values
my_dict["city"]="Chandigarh"
print(my_dict)
details["city"]="Chandigarh"
print(details)

#del the key-value pair
#1
details.popitem()
print(details)
#method2
details.pop("name")
print(details)
#method3
#del details["city"]
#print(details)

# keys in our dictionar
if "name" in my_dict:
    print(details["name"]) #if this statement run successfully means keys in the list
else:
    print("not in the my dict")
#another way
try:
    print(my_dict["name"])
except:
    print("Error")

#loops through dictionary
for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)



for key,value in my_dict.items():
    print(key)   

#copy the dictionary
my_dict_copy=my_dict.copy()
my_dict_copy["email"]="daga@gagam.com"

#update of the list
my_dict={"name":"sagar","last_name":"singh","age":30}
new_data={"name":"sagar","last_name":"singh","email":"daga@d.com"}
my_dict.update(new_data)
print(my_dict)

#possible key type
letters={2:2,6:4,3:2}
print(letters)
values=letters[2]
print(values)
#key can be tuple but not list beacause list mutable can be changed after assiing
my_tuple=(1,2)
add={my_tuple:3}
print(add)

my_list=[1,2]
add1={my_list:3}
print(add1)



#json : javascript object notation
#creation
import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
#convert to json
person_json=json.dumps(person)
#use different formating style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
#reult
print(person_json)
print(person_json2)

#saving and reading user-generated data
import json
username=input("what is your name")
filename="username.json"
with open(filename,"w") as file:
    json.dump(username,file)
    print("we will remeber you when you come back"+username+"!")

with open("username.json") as file:
  detail=json.load(file)
  print(detail)
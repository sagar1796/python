#saving and reading user-generated data
import json
username=input("what is your name")
filename="username.json"
with open(filename,"w") as file:
    json.dump(username,file)
    print("we will remeber you when you come back"+username+"!")
todos=[]
while True:
    user_action=input("enter add , show, exit :")
    user_action=user_action.strip()
    
    match user_action:
        case "add":
            todo=input("Enter a todo")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
        case _:
            print("please ente your valid entry")
print("bye")
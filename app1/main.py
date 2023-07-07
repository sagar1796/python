todos=[]
while True:
    user_action=input("enter add , show, exit ,edit:")
    user_action=user_action.strip()
    
    match user_action:
        case "add":
            todo=input("Enter a todo")
            todos.append(todo)
        case "show":
            print(todos)
        case "completed":
            completed=int(input("enter your number you've completed :"))
            del todos[completed-1]
        case "exit":
            break
        case _:
            print("please ente your valid entry")
print("bye")
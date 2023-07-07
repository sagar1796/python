todos=[]
while True:
    user_action=input("enter add , show, exit ,edit:")
    user_action=user_action.strip()
    
    match user_action:
        case "add":
            todo=input("Enter a todo") +"\n"
            file=open("app1\\todos.txt","r")
            todos=file.readlines()
            file.close()
            todos.append(todo)
            
            file=open("app1\\todos.txt","w")
            file.writelines(todos)
            file.close()
        case "show":
              for index,item in enumerate(todos):
                print(f"{index}-{item}")
                print(f"lenght of list is {index+1}")
        case "completed":
            completed=int(input("enter your number you've completed :"))
            todos.pop(completed-1)
        case "exit":
            break
        case _:
            print("please ente your valid entry")
print("bye")
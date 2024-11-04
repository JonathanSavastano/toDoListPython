# to do list app

# initialize lists
toDo = []
completed = []


# function to display lists
def displayLists():
    print("To Do: ", toDo)
    print("Completed: ", completed)


#function to add to list
def addTask():
    userInput = input("What would you like to add to your list?").lower()
    if userInput not in toDo:
        toDo.append(userInput)
        print("Added task to list: ", toDo)
    else:
        print("That task is already in your list!")


# function to add task to completed list
def completeTask():
    userInput = input("What task would you like to mark as complete?").lower()
    if userInput in completed:
        print("That task is already marked as completed")
    elif userInput not in toDo or completed:
        print("There is no such task.")
    elif userInput in toDo:
        toDo.remove(userInput)
        completed.append(userInput)
        print(userInput, " has been added to completed tasks.")
        print("Completed Tasks: ", completed)


# function to delete tasks
def deleteTask():
    print("To do: ", toDo, "Completed: ", completed)
    userInput = input("What task would you like to delete?").lower()
    if userInput not in toDo or completed:
        print("That task does not exist.")
    elif userInput in toDo:
        toDo.remove(userInput)
    elif userInput in completed:
        completed.remove(userInput)


# main function
def main():
    while True:
        print("Welcome to your to do list! What would you like to do today?")
        userInput = input("You can say: display, add, complete, delete, save, or load. Press q to exit the program.").lower()
        if userInput == "display":
            displayLists()
        elif userInput == "add":
            addTask()
        elif userInput == "complete":
            completeTask()
        elif userInput == "delete":
            deleteTask()
        elif userInput == "q":
            exit()
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
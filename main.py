# to do list app

# initialize lists
toDo = []
completed = []


#function to add to list
def addTask():
    userInput = input("What would you like to add to your list?")
    if userInput not in toDo:
        toDo.append(userInput)
        print("Added task to list: ", toDo)
    else:
        print("That task is already in your list!")


# TODO create function to add task to completed list

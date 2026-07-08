to_Do_List = []

def add_Task(recieved_List):
    task_Name = input("What to do: ")
    priority = input("Task Priority(High, Medium, Low): ")
    new_Task = {
        'task' : task_Name,
        'pri' : priority
    }   
    recieved_List.append(new_Task)

def view_Task(recieved_List):
        if len(recieved_List) == 0:
            print("-------------------")
            print("You have no task!")
            print("===================")
        else:
            print("{:<15}{:<10}".format("Task", "Priority"))
            for tasks in recieved_List:
                print("{:<15}{:<10}".format(tasks["task"], tasks["pri"]))
def menu():
    print("1. Add a Task.")
    print("2. View All Tasks.")
    print("3. Delete a Task.")
    print("4. Filter by Priority.")
    print("5. Exit.")
def main():
    while True:
        menu()
        user_input = input("Select an option(1-5): ")
        if user_input == '1':
            add_Task(to_Do_List)
        if user_input == '2':
            view_Task(to_Do_List)
        elif user_input == '5':
            break
# REVERT
# <================================================MAIN PROGRAM STARTS HERE================================================>
main()
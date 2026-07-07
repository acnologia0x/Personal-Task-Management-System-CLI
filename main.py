to_Do_List = []

def add_Task(recieved_List):
#  I did NOT need to loop through the existing list to add a new task. I simply need to capture the input and append it.
    for tasks in recieved_List:
        if len(tasks) == 0:
            print("=================")
            print("No tasks.")
            print("=================")
        else:
            #By putting input() inside of an else statement I am basically saying only ask to add task if the task is not empty lol it defeats the whole point of adding tasks to an empty list.
            task_Name = input("What to do: ")
            priority = input("Task Priority(1.High, 2.Medium, 3.Low): ")
            new_Task = {
                'task' : task_Name,
                'pri' : priority
            }   
            recieved_List.append(new_Task)
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
        elif user_input == '5':
            break

# <================================================MAIN PROGRAM STARTS HERE================================================>
main()
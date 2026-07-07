to_Do_List = []

def add_Task(recieved_List):
    print("It worked!")

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
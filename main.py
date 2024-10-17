from modules import functions
import time

now = time.strftime("%Y.%b.%d - %H:%M:%S")
print(f"The time is {now}")

def principal():
    # Use a breakpoint in the code line below to debug your script.
    # print("Enter task to do: ")  # Press Ctrl+F8 to toggle the breakpoint.

    while True:
        # Get user input and strip space characters from it
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip() # remove trailing spaces

        if user_action.startswith('add'):
            todo = user_action[4:] + "\n"

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos)

        elif user_action.startswith('show'):
            todos = functions.get_todos()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # new_todos = [item.strip('\n') for item in todos] # list
            # comprehension

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                number -= 1

                todos = functions.get_todos()

                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo + '\n'

                functions.write_todos(todos)
            except ValueError:
                print('Invalid todo number selection.')
                continue

        elif user_action.startswith('complete'):
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            message = f"Todo {todo_to_remove} was removed from the list."
            todos.pop(index)

            functions.write_todos(todos)

            print(message)

        elif user_action.startswith('exit'):
            print("Bye!")
            break

        else:
            print("Selection is not valid! Select again")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    principal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

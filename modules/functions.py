FILEPATH = 'files/todos.txt'

print('Hello from functions.')
def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the list of lines in the file."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Writes a list of todos in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
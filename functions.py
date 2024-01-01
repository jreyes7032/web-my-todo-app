# match user_action: case (case _:); "|" bitwise or
# for item in todos:
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        todos_local = [item.strip('\n') for item in todos_local]
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        todos_arg = [item + '\n' for item in todos_arg]
        file_local.writelines(todos_arg)


print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())

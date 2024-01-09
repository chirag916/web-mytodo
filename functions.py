FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read the txt file and  return
    to do file lists
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items in the list or say in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == "__main__":
    print("hello")

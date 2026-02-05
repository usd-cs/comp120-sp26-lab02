from sys import argv

def print_file(filename: str) -> None:
    """Prints out the contents of a file.

    Args:
        filename (str): The name of the file to open and print out.
    """    
    f = open(filename, 'r')
    for line in f:
        print(line)


print(type(argv))
print(argv)
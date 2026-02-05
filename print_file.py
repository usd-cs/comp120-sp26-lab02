from sys import argv

def print_file(filename: str) -> None:
    """Prints out the contents of a file.

    Parameters:
        filename (str): The name of the file to open and print out.

    Examples:
        >>> print_file('haiku.txt')
        An old silent pond
        A frog jumps into the pond-
        Splash! Silence again.
    """    
    f = open(filename, 'r')
    for line in f:
        print(line, end='')


def main() -> None:
    print(type(argv))
    print(argv)

if __name__ == "__main__":
    main()
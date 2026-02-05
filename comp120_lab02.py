import turtle

def difference(x, y):
    """Calculates the absolute difference between two numbers.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Absolute difference between x and y
    """
    diff = abs(y - x)
    return diff

def draw_square(my_turtle, size):
    for i in range(4):
        my_turtle.forward(size)
        my_turtle.left(90)


def sum(nums):
    """Calculates the sum a list of integers.

    Args:
        nums (list[int]): The list of integers to sum up.

    Returns:
        int: The sum

    >>> sum([5])
    5
    >>> sum([1, 5, 7])
    13
    """    
    total = 0
    for n in nums:
        total += n
    
    return total

def count_matches(target: int, nums: list[int]) -> int:
    """Finds the number of times target occurs in the given list (nums).

    Args:
        target (int): The number to look for.
        nums (list[int]): The list of numbers to search through.

    Returns:
        int: Number of times target appears in nums
    
    >>> count_matches(5, [1, 5, 3, 5, 6])
    2
    >>> count_matches(7, [1, 5, 3, 5, 6])
    0
    >>> count_matches(3, [1, 5, 3, 5, 6])
    1
    """

    matches = 0
    for n in nums:
        if n == target:
            matches += 1

    return matches

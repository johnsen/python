


def add_lists(a, b):
    """
      >>> add_lists([1, 1], [1, 1])
      [2, 2]
      >>> add_lists([1, 2], [1, 4])
      [2, 6]
      >>> add_lists([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
    """
    for index, value in enumerate(a):
        return a[index] = value * b
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    





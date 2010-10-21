import string

def myreplace(old, new, s):
    """
     >>> myreplace(',', ';', 'this, that, and, some, other, thing')
     'this; that; and; some; other; thing'
     >>> myreplace(' ', '**', 'Words will now be separated by stars.')
     'Words**will**now**be**separated**by**stars.'
    """
 
    return string.replace(s, old, new)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

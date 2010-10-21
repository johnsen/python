


#"""
#  >>> nlist[2][1]
#  0
#  >>> nlist[0][2]
#  17
#  >>> nlist[1][1]
#  5
#"""

#nlist = [0, 1, 17, [0, 5], [0, 0]]
#for index, in value in enumerate(nlist):
#    print index, value

numbers = [1, 2, 3, 4, 5]

for index, value in enumerate(numbers):
    print numbers[index] = value**2
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()




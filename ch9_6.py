
"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
"""

junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
a = 2
b = 7


"""
  >>> nlist[2][1]
  0
  >>> nlist[0][2]
  17
  >>> nlist[1][1]
  5
"""

nlist = [0, 0, 0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()




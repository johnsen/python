def longestword(wordset):
    
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    if len(wordset[0]) < len(wordset[1]) > len(wordset[2]):
        return len(wordset[1] 
  #  elif len(wordset[1]) < len(wordset[0]) > len(wordset[2]):
   #     return len(wordset[0])
   # else:
   #     return len(wordset[2])

 #   if __name__ == '__main__':
  #  import doctest
   # doctest.testmod()

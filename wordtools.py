import string

def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """

    
    return word.strip('@$#,()!?+="')


def extract_words(s):
    """
      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """

    str = s
    str = ''.join([ c for c in str if c not in ('@', '.', ',', "'", '"', '!', '?', '&')])
    str = str.lower()
 #   str = str[6].split('--')
    str = str.split(' ')
#    str =  str.split('')
    return str

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

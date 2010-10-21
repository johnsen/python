def doe_twee_keer(f):
      f()
      f()


def print_spam():
    print 'spam'

doe_twee_keer(print_spam)

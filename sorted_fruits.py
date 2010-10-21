import string

def sortfruits(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
#    text = infile.readlines()
#    text = sorted(text)
#    outfile.writelines(text)
#    infile.close()
#    outfile.close()
    outfile.writelines(sorted(infile))

sortfruits('/home/d/python/unsorted_fruits.txt', '/home/d/python/sorted_fruits.txt')

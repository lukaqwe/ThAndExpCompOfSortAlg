# This creates a file with sorted integers

from random import randint
n1 = 1000
n2 = 5000
n3 = 10000
n4 = 15000
n5 = 25000

n = n1  # here put the size
filename = 'sorted' + str(n) + '.txt'
with open(filename, 'w') as file:
    for i in xrange(n):
        file.write(str(i)+'\n')

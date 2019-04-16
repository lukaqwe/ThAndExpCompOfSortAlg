# This creates a file with random integers

from random import randint

n1 = 500
n2 = 1000
n3 = 5000
n4 = 10000
n5 = 15000
n6 = 25000
n7 = 50000
n8 = 100000
n9 = 500000
n10 = 1000000

n = n1  # here put the size
filename = 'random' + str(n) + '.txt'

with open(filename, 'w') as file:
    for i in xrange(n):
        file.write(str(randint(0, n))+'\n')

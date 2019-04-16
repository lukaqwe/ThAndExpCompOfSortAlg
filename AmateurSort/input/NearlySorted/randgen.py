# This creates a file with nearly sorted integers

from random import randint

n1 = 5000
n2 = 10000
n3 = 25000
n4 = 50000
n5 = 100000

n6 = 100000
n7 = 500000
n8 = 1000000
n9 = 5000000
n10 = 10000000
n11 = 50000000

n = n1  # here put the size
range = 5  # here put the range of integers

filename = 'nearly' + str(n) + '.txt'
with open(filename, 'w') as file:
    for i in xrange(n):
        file.write(str(randint(i-range, i))+'\n')

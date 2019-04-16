# This creates a file with random integers between 0 1nd 150

from random import randint

n1 = 100000
n2 = 500000
n3 = 1000000
n4 = 5000000
n5 = 10000000
n6 = 50000000
n7 = 100000000

n = n1
range = 150  # here put the range of integers

filename = 'ages' + str(n) + '.txt'

with open(filename, 'w') as file:
    for i in xrange(n):
        file.write(str(randint(0, range))+'\n')

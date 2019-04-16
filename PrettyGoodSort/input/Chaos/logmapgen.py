# This creates a file with random real numbers from 0 to 1

import time
n1 = 50000
n2 = 100000
n3 = 500000
n4 = 1000000
n5 = 5000000
n6 = 10000000
n7 = 50000000

n = n1  # here put the size of the list

r = 3.9  # here put the chaotic factor which starts at 3.57 and maximum is 4

x = time.time()
x = x - int(x)  # planting the seed

filename = 'chaos' + str(n) + '.txt'


def logmap(X, R):
    return R*X*(1-X)


with open(filename, 'w') as file:
    for i in range(n):
        x = logmap(x, r)
        file.write(str(x)+'\n')

# here import whatever algorithm you want
from quick import quick_sort
import sys
import time
A = []
path = "PrettyGoodSort/input/AlreadySorted/25000.txt"
with open(path, 'r') as file:
    A = file.readlines()
    for i in range(len(A)):
        A[i].strip()
        A[i] = float(A[i])

sys.setrecursionlimit(30000)  # be careful with this one


start = time.time()
A = quick_sort(A, 0, len(A)-1)  # here call whatever algorithm you've chosen
end = time.time() - start
print(end)

# you can uncomment this block if want to store the result in another file
# with open('output.txt', 'w') as file:
#    for n in A:
#        file.write(str(n)+'\n')

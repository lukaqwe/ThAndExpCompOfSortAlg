from binsertion import binsertion_sort  # here import whatever algorithm you want
import time
A = []
path = "/home/luca/Projects/Experiments/AmateurSort/input/NearlySorted/binsertion/nearly50000.txt"

with open(path, 'r') as file:
    A = file.readlines()
    for i in range(len(A)):
        A[i].strip()
        A[i] = int(A[i])

start = time.time()
A = binsertion_sort(A)  # here call whatever algorithm you've chosen
end = time.time() - start
print(end)

# you can uncomment this block if want to store the result in another file
# with open('output.txt', 'w') as file:
#    for n in A:
#        file.write(str(n)+'\n')

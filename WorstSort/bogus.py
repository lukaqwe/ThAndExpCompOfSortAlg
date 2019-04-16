import math
from random import shuffle
import time

L1 = [3, 2, 1]
L2 = [5, 4, 3, 2, 1]
L3 = [7, 6, 5, 4, 3, 2, 1]
L4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
L5 = [11, 10, 9, 8, 7, 6, 5, 4, 2, 1]
L6 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
L7 = [4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]


def check(A):
    n = len(A)
    for i in range(1, n):
        if A[i-1] > A[i]:
            return True
    return False


def bogo_sort(A):
    k = 0
    while check(A):
        k += 1
        shuffle(A)
    return k  # or return A if you want the array


def is_not_in(A, num):
    if num in A:
        return False
    return True


def avg(A):
    avg = (min(A)+max(A))//2
    while is_not_in(A, avg):
        avg += 1
    return avg


def test_bogus(Attempts, A):
    Time = {}
    for i in range(Attempts):
        start = time.time()
        k = bogo_sort(A[:])
        end = time.time() - start
        Time[k] = end

    print(max(Time.keys()), Time[max(Time.keys())])
    print(avg(Time.keys()), Time[avg(Time.keys())])
    print(min(Time.keys()), Time[min(Time.keys())])


def P_k(n, k):  # calculates P_k for distinct elements ,requires tough floating point copmutations
    return pow((1-(1 / math.factorial(n))), k)


def calc_Pk():
    K = {3: 29, 5: 108, 7: 5002, 9: 275114, 11: 6468303}
    P = []
    for n in K.keys():
        print(P_k(n, K[n]))

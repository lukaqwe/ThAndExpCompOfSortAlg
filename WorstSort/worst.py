import itertools
import time


def fact_sort(A, lvl):
    if lvl == 0:
        bubble_sort(A)
        return in_depth(A)[0][0]
    else:
        G = [list(p) for p in itertools.permutations(A)]
        return fact_sort(G, lvl-1)


def exp_sort(A, lvl):
    global Initial
    if lvl == 0:
        bubble_sort(A)
        for p in in_depth(A):
            if check(Initial, p):
                return p
    else:
        G = [list(p) for p in itertools.product(A, repeat=len(A))]
        return exp_sort(G, lvl-1)


start = time.time()
Initial = [6, 5, 4, 3, 2, 1]
print(exp_sort(Initial, 1))
end = time.time()-start
print(end)


def in_depth(A):
    # A way to get the list of lists in the big nested list of lists of lists of lists of lists of lists ...
    if type(A[0][0]) == int:
        return A
    return in_depth(A[0])


def check(A, X):
    B = A[:]
    for i in range(len(X)):
        for j in range(len(B)-1, -1, -1):  # in this way I avoid IndexError
            if X[i] == B[j]:
                B.pop(j)
                break
    if len(B) == 0:
        return True
    return False


def compare(A, B):
    if type(A) == int:  # if elements are integers
        return A < B
    # if they are lists perform a lexicographic comparison
    for i in range(len(A)):
        if compare(A[i], B[i]):
            return True
        elif compare(B[i], A[i]):
            return False
    return False  # all elements are equal


def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare(A[j+1], A[j]):
                A[j], A[j+1] = A[j+1], A[j]

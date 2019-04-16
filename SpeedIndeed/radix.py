# from counting import counting_sort # if you want to use counting sort uncomment the import


def radix_sort(A):
    n = len(A)
    if n == 1:
        return A
    max_dig = nr_of_digits(max(A))+1  # you can also do len(str(max(A)))+1
    Result = []
    for dig in range(1, max_dig):
        Dig_list = []
        for el in A:
            if len(str(el)) == dig:
                Dig_list.append(el)
        Dig_list.sort()  # you can do also counting_sort(Dig_list) but this is more efficient
        Result += Dig_list
    return Result


def nr_of_digits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

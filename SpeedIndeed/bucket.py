
def bucket_sort(A):
    # My buckets have the range 10
    if len(A) == 1:
        return A
    Buckets = [[] for x in xrange(max(A)//10)]+[[]]
    for num in A:
        bucket_nr = num//10
        Buckets[bucket_nr].append(num)
    for bucket in Buckets:
        bucket.sort()
    return sum(Buckets, [])

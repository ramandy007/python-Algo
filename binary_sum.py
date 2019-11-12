def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start,stop] """
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start+stop)//2
        return binary_sum(S, start, mid)+binary_sum(S, mid, stop)


S = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_sum(S, 0, len(S)))
print(S)

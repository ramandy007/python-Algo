def reverse(S, start, stop):
    """REVERSE ELEMENTS IN IMPLICIT SLICE S[START:STOP]"""
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


S = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(S, 0, len(S))
print(S)

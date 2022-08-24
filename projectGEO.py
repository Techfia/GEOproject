import json
from itertools import groupby

A1 = [3, 4, 3, 2, 3, -1, 3, 3]
A2 = [1, 2, 1]
A3 = [0, 0, 2, 1, 3]


def solution(A):
    if len(A) == 1:
        return 0

    dominator = -1
    dominatorCount = 0
    for k, v in groupby(sorted(A)):
        length = len(list(v))
        if (length > dominatorCount):
            dominator = k
            dominatorCount = length

    if dominator == -1:
        return -1

    index = -1
    for i in range(0, len(A) - 1):
        if (A[i] == dominator):
            if (i == 0 or A[i] == A[i + 1]):
                index = i

    return index if (dominatorCount > (len(A) / 2)) else -1


print(solution(A1))
print(solution(A2))
print(solution(A3))

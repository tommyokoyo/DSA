from typing import List


def find_maximal(arr: list) -> List:
    arr.sort(reverse=True)
    subset_a = []
    n = 0

    while arr:
        subset_a.insert(0, arr.pop(n))
        if sum(subset_a) > sum(arr):
            break
    return subset_a


print(find_maximal([3, 7, 5, 6, 2]))

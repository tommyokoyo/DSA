def countpairs(p: int, k: int, a: list) -> int:
    count = 0
    array_len = len(a)
    array_squared = [i ** 2 for i in a]
    if array_len >= 2 and p >= 2:
        for i in range(array_len):
            for j in range(i + 1, array_len):
                if ((a[i] + a[j]) * ((array_squared[i]) + (array_squared[j]))) % p == k:
                    count += 1
    return count


n, p, k = map(int, input().split())
a = list(map(int, input().split()))
print(countpairs(p, k, a))

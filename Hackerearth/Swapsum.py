def maximum_sum(a: list, b: list, operations: int) -> int:
    """
        Finds the maximum sum of array A after performing at most K operations
        :param a:
        :param b:
        :param operations:
        :return:
    """
    sum_a = sum(a)

    difference = [(b[i] - a[i], i) for i in range(len(a))]
    difference.sort(reverse=True)

    for value, i in difference:
        if operations == 0 or value <= 0:
            break
        a[i], b[i] = b[i], a[i]
        sum_a += value
        operations -= 1

    return sum_a


test_cases = int(input())

for _ in range(test_cases):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(maximum_sum(A, B, K))

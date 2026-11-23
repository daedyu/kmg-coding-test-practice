n, m = map(int, input().split())

arr = list(set(map(int, input().split())))

arr.sort()

def backtrack(first_arr: list, idx, result: list):
    if idx == 0:
        print(' '.join(map(str, result)))
        return
    for i in first_arr:
        if result and i < result[-1]:
            continue
        backtrack(first_arr, idx - 1, result + [i])

backtrack(arr, m, [])
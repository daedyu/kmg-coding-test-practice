n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

def backtrack(first_arr: list, idx, result):
    if idx == 0:
        print(' '.join(map(str, result)))
        return
    for i in first_arr:
        new_arr = first_arr.copy()
        new_arr.remove(i)
        backtrack(new_arr, idx - 1, result + [i])

backtrack(arr, m, [])
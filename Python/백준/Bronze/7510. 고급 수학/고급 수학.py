n = int(input())

for i in range(1, n + 1):
    print(f'Scenario #{i}:')
    arr = list(map(int, input().split()))
    max_data = max(arr)
    arr.remove(max_data)
    print('yes' if max_data ** 2 == arr[0] ** 2 + arr[1] ** 2 else 'no')
    print()
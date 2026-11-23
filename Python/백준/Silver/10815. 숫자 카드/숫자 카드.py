import sys
input = sys.stdin.readline

input()
arr = set(map(int, input().split()))

input()
arr2 = list(map(int, input().split()))

for i in arr2:
    if arr.intersection({i}):
        print(1, end=' ')
    else:
        print(0, end=' ')
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

data = dict()

for _ in range(n):
    site, pwd = input().rstrip().split()
    data[site] = pwd

for _ in range(m):
    print(data[input().rstrip()])

import sys
import math

input = sys.stdin.readline

def round_half_up(x):
    return math.floor(x + 0.5)

n = int(input())

if n == 0:
    print(0)
    sys.exit()

arr = [int(input()) for _ in range(n)]
arr.sort()

cut = int(round_half_up(n * 15 / 100))
s = arr[cut:n-cut]

print(round_half_up(sum(s) / len(s)))

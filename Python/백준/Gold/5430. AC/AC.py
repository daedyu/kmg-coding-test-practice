import sys
from collections import deque
input = sys.stdin.readline

def data_cnt(stack: list, fnc: list) -> str:
    stack = deque(stack)
    rev = False
    for f in fnc:
        if f == 'R':
            rev = not rev
        elif f == 'D':
            if not stack:
                return 'error'
            if rev:
                stack.pop()
            else:
                stack.popleft()
    if rev:
        return '[' + ','.join(reversed(stack)) + ']'
    else:
        return '[' + ','.join(stack) + ']'


for _ in range(int(input())):
    fnc = input().rstrip()
    n = int(input())
    arr = list(filter(None, input().rstrip()[1:-1].split(',')))
    print(data_cnt(arr, fnc))
import sys

input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()
n = len(boom)

stack = []

for i in string:
    stack.append(i)
    len_data = len(stack)
    while len_data >= n and stack[len_data-n:len_data] == list(boom):
        for _ in range(n):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
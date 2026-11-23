import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    n = input().rstrip().split()

    if n[0] == 'push':
        stack.append(n[1])
    elif n[0] == 'pop':
        if not stack:
            print(-1)
            continue
        print(stack.pop())
    elif n[0] == 'size':
        print(len(stack))
    elif n[0] == 'empty':
        print(0 if stack else 1)
    else:
        if not stack:
            print(-1)
            continue
        print(stack[-1])
import sys

input = sys.stdin.readline

def balance(s: list) -> bool:
    stack = []
    new_s = []
    for i in range(len(s) - 1):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                return False
            data = stack.pop()
            if data != '(':
                return False
            if not balance(new_s):
                return False
        elif s[i] == '[':
            stack.append(s[i])
        elif s[i] == ']':
            if not stack:
                return False
            data = stack.pop()
            if data != '[':
                return False
            if not balance(new_s):
                return False
        else:
            new_s.append(s[i])
    if stack:
        return False
    return True

while True:
    n = input().rstrip('\n')
    if n == '.':
        exit()
    if list(n)[-1] != '.':
        print('no')
        exit()
    print('yes' if balance(list(n)) else 'no')
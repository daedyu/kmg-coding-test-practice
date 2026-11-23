order = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1, ')': -2}
stack = []
result = ''

for i in input():
    if not i in '+-*/()':
        result += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            result += stack.pop(-1)
        stack.pop(-1)
    else:
        while stack and order[stack[-1]] >= order[i]:
            result += stack.pop(-1)
        stack.append(i)

while stack:
    result += stack.pop(-1)

print(result)
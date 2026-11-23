from math import factorial

n = list(str(factorial(int(input()))))

n.reverse()

result = 0

for i in n:
    if i != '0':
        break
    result += 1

print(result)
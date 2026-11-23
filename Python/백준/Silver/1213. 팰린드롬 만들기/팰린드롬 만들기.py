from collections import Counter

n = input()

data = dict(Counter(n))

cnt = ''

for k, v in data.items():
    if v & 1:
        if cnt != '':
            print("I'm Sorry Hansoo")
            exit()
        cnt = k
        data[cnt] -= 1

result = ''

for k in sorted(data.keys()):
    if data[k] > 0:
        result += k * (data[k] // 2)
        data[k] -= 0

print(result + cnt + result[::-1])
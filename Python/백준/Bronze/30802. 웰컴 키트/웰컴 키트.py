n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

cnt = 0

for i in arr:
    temp = i//a
    temp += 1 if i % a != 0 else 0
    cnt += temp

print(cnt)
print(n//b, n%b)
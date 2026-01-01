n, m = map(int, input().split())

not_hear_arr = set()
not_seen_arr = set()

for _ in range(n):
    not_hear_arr.add(input())

for _ in range(m):
    not_seen_arr.add(input())

result = sorted(not_hear_arr.intersection(not_seen_arr))

print(len(result))
print(*result, sep="\n")
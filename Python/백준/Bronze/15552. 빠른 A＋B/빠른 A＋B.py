import sys
input, print = sys.stdin.readline, sys.stdout.write
for _ in range(int(input())):
    print(str(sum(map(int, input().rstrip().split()))) + '\n')
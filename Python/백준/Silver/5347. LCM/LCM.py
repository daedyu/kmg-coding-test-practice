def lcm(a, b):
  return (a * b) // gcd(a, b)

def gcd(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))
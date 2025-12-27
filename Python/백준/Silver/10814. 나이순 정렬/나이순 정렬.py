arr = list()

for i in range(int(input())):
    age, name = input().split()
    age = int(age)
    arr.append((i, age, name))

arr.sort(key=lambda x: (x[1], x[0]))

for data in arr:
    print(data[1], data[2])
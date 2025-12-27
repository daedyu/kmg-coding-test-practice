n = int(input())

for _ in range(n):
    fibo_number = int(input())
    dp_zero = [0] * (fibo_number + 1)
    dp_one = [0] * (fibo_number + 1)
    for i in range(fibo_number + 1):
        if i == 0:
            dp_zero[i] = 1
        elif i == 1:
            dp_one[i] = 1
        else:
            dp_one[i] = dp_one[i-1] + dp_one[i-2]
            dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
    print(dp_zero[fibo_number], dp_one[fibo_number])
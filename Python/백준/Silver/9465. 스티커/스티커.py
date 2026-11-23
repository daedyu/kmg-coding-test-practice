for _ in range(int(input())):
    m = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(m)]

    dp[0][0] = arr1[0]
    dp[0][1] = arr2[0]

    for i in range(1, m):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr1[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + arr2[i])

    print(max(dp[m-1]))
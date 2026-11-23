while True:
    n = input()

    if n == "0":
        break

    k = reversed(list(n))
    k = "".join(k)

    print("yes" if n == k else "no")
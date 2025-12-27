text = list()
for i in range(int(input())):
    data = input()
    if i == 0:
        text = list(data)
        continue

    for i in range(len(data)):
        if text[i] != data[i]:
            text[i] = "?"
print(''.join(text))
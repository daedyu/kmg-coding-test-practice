'''
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###
'''

numbers = [
    [
        "###",
        "#.#",
        "#.#",
        "#.#",
        "###"
    ],
    [
        "..#",
        "..#",
        "..#",
        "..#",
        "..#"
    ],
    [
        "###",
        "..#",
        "###",
        "#..",
        "###"
    ],
    [
        "###",
        "..#",
        "###",
        "..#",
        "###"
    ],
    [
        "#.#",
        "#.#",
        "###",
        "..#",
        "..#"
    ],
    [
        "###",
        "#..",
        "###",
        "..#",
        "###"
    ],
    [
        "###",
        "#..",
        "###",
        "#.#",
        "###"
    ],
    [
        "###",
        "..#",
        "..#",
        "..#",
        "..#"
    ],
    [
        "###",
        "#.#",
        "###",
        "#.#",
        "###"
    ],
    [
        "###",
        "#.#",
        "###",
        "..#",
        "###"
    ],
]

def check_can_number(array: list):
    available = []
    num = 0

    for data in numbers:
        non = False
        for i in range(5):
            for j in range(3):
                if array[i][j] == '#' and data[i][j] == '.':
                    non = True
                    break
            if non:
                break
        if not non:
            available.append(num)
        num += 1
    return available

n = int(input())

arr = []

for _ in range(5):
    arr.append(input())

result = 0

tmp_s = 10 ** (n-1)

for i in range(0, n * 3 + (n - 1), 4):
    temp = []
    for j in range(5):
        temp.append(arr[j][i:i + 3])

    tmp_result = check_can_number(temp)
    if sum(tmp_result) == 0:
        print(-1)
        exit()
    result += (sum(tmp_result) / len(tmp_result)) * tmp_s

    tmp_s //= 10

print(result)
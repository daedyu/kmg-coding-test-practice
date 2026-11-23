class SegmentTree:
    def build(self, arr: list, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.build(arr, node * 2, start, mid) + self.build(arr, node * 2 + 1, mid + 1, end)

        return self.tree[node]

    def __init__(self, arr: list):
        self.tree = [0] * (4 * n)
        self.build(arr, 1, 0, n - 1)

    def get_sum(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.get_sum(node * 2, start, mid, left, right) + self.get_sum(node * 2 + 1, mid + 1, end, left, right)

    def update(self, node, start, end, index, value):
        if start > index or end < index:
            return self.tree[node]
        if start == end:
            self.tree[node] = value
            return value
        mid = (start + end) // 2
        self.tree[node] = self.update(node * 2, start, mid, index, value) + self.update(node * 2 + 1, mid + 1, end, index, value)
        return self.tree[node]

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

segment_tree = SegmentTree(arr)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update(1, 1, n, b, c)
    if a == 2:
        print(segment_tree.get_sum(1, 1, n, b, c))
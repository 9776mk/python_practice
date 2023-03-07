# N = int(input())
# list_ = []

# for i in range(N):
#     list_.append(input().split())

N = 8
list_ = [
    ["1", "1", "0", "0", "0", "0", "1", "1"],
    ["1", "1", "0", "0", "0", "0", "1", "1"],
    ["0", "0", "0", "0", "1", "1", "0", "0"],
    ["0", "0", "0", "0", "1", "1", "0", "0"],
    ["1", "0", "0", "0", "1", "1", "1", "1"],
    ["0", "1", "0", "0", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1", "1", "1", "1"],
]

# cut_ = [[False] * N for _ in range(N)]

cut_ = [
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
]

print(list_)
print(cut_)

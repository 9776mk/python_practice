n, m = map(int, input().split())
#n, m = 5, 7

bbang_ = [list(input()) for _ in range(n)]
'''
bbang_ = [
    ['0', '0', '1', '0', '0', '0', '0'], 
    ['0', '1', '1', '1', '0', '1', '0'], 
    ['1', '1', '1', '1', '1', '1', '1'], 
    ['0', '1', '1', '1', '0', '1', '0'], 
    ['0', '0', '1', '0', '0', '0', '0']
]
'''

dropped_bbang = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        dropped_bbang[i][j] = bbang_[i][m-j-1]


for list in bbang_:
    for i in list:
        print(i, end='')
    print()

print('답')

for list in dropped_bbang:
    for i in list:
        print(i, end='')
    print()

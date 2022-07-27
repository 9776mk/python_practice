afterimage = input()

l_punch = 0
r_punch = 0

idx_l = afterimage.index('(')
idx_r = afterimage.index(')')

for i in range(0, idx_l):
    if afterimage[i] == '@':
        l_punch += 1        

for j in range(len(afterimage)-1, idx_r,-1):
    if afterimage[j] == '@':
        r_punch += 1

print(l_punch, r_punch)
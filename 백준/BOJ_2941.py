S = input()
croatian_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
new_S = ''
n = 0

while n <= len(S)-1:
    if S[n:n+3] in croatian_alpha:
        cnt += 1
        n += 3
    elif S[n:n+2] in croatian_alpha:
        cnt += 1
        n += 2
    else:
        cnt += 1
        n += 1
print(cnt)
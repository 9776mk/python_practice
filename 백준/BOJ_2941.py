S = input()
croatian_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
new_S = ''

# 2글자를 비교해서 만약 croatian_alpha에 해당한다면 새로운 리스트에 추가x count +=1 

for n in range(0, len(S)-1):
    if S[n:n+2] in croatian_alpha:
        del S[n:n+2]
        cnt += 1
    else:
        continue

print(S)
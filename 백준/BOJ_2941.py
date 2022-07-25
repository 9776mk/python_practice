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

'''
# replace 함수를 이용하여, croatian_alpha에 있는 것들을 한 글자로 바꿔 길이를 출력함.
word = input()
for i in croatian_alpha :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
'''
S = input()

# 크로아티아 알파벳을 리스트에 만듦
croatian_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 알파벳 카운트할 변수 cnt 선언
cnt = 0
# 문자열 S내에서 중복을 피하기 위한 index 설정
n = 0

# n이 끝까지 둘러보면 while문 종료
while n <= len(S)-1:
    # 크로아티아 알파벳이 3글자, 2글자가 있으므로 큰 글자 먼저
    # 만약 n에서 시작한 3글자가 크로아티아 리스트에 있으면 cnt를 1더하고, 3글자 뒤로 이동
    if S[n:n+3] in croatian_alpha:
        cnt += 1
        n += 3
    # 만약 n에서 시작한 3글자가 리스트에 없지만 2글자가 크로아티아 리스트에 있으면 cnt를 1더하고, 2글자 뒤로 이동
    elif S[n:n+2] in croatian_alpha:
        cnt += 1
        n += 2
    # 만약 n에서 시작한 3글자,2글자가 크로아티아 리스트에 없으면 cnt를 1더하고, 1글자 뒤로 이
    else:
        cnt += 1
        n += 1
print(cnt)
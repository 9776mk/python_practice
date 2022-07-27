# 2차원 리스트로 입력 받음
score_list = [list(map(str, input())) for _ in range(5)]

# 길이가 제일 긴 리스트의 길이를 구하고, max_len에 대입
len_list = []
for i in range(5):
    len_list.append(len(score_list[i]))
max_len = max(len_list)

 # max_len과 길이가 다른 리스트에 '*'를 추가시켜 길이를 똑같이 만듦
for i in range(5):
    if len(score_list[i]) != max_len:
        for j in range(max_len - len(score_list[i])):
            score_list[i].append('*')

# 2차원 리스트 [0][0] ~ [5][max_len] 새로운 리스트에 추가
sero_list = []
for n in range(max_len):
    for m in range(5):
        sero_list.append(score_list[m][n])

# *면 continue, 문자면 그대로 출력
for char in sero_list:
    if char != '*':
        print(char, end='')
    else:
        continue
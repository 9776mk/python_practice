# 참가자 수 N 입력
N = int(input())

# 각 플레이어의 수를 리스트로 저장
num_list = []

for _ in range(N):
    num_list.append(list(input().split()))

# 총 3개의 열로 리스트를 만들어서 
col_list = [[],[],[]]
for i in range(3):
    for j in range(N):
        # col_list에 있는 엳들을 저장
        col_list[i].append(num_list[j][i])

# 값을 저장할 리스트 생성
answer_list = [0] * N

# 열들의 집합에서 각각의 요소들을 count 했을 때 1, 즉 한 개인 경우 answer_list에 그 값을 더함
for i in range(3):
    for j in range(N):
        if col_list[i].count(col_list[i][j]) == 1:
            answer_list[j] += int(col_list[i][j])

# 하나씩 출력
for i in range(N):
    print(answer_list[i])
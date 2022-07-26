# 2차원 배열로 입력 받음. 
score_list = [list(map(int, input().split())) for _ in range(5)]

max_sum = 0
max_index = 0

for i in range(5):
    # 만약 리스트의 합이 max_sum 보다 크다면, max_sum과 max_index에 저장
    if sum(score_list[i]) > max_sum:
        max_sum = sum(score_list[i])
        max_index = i

print(f'{max_index+1} {max_sum}')
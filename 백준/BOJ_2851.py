list_score = []
# 버섯 10개의 점수를 입력받음
for i in range(10):
    list_score.append(int(input()))

score = 0
tmp_score = 0
tmp_sum_n = 0
tmp_sum_n_minus_1 = 0

# 1부터 10까지 버섯의 합을 구함.
for i in range(10):
    
    tmp_sum_n += list_score[i]
    # n까지 먹었을 때 100이상이 된다면
    if tmp_sum_n >= 100:
        # n-1까지 먹었을 때의 점수와 n까지의 점수를 비교
        # (n-1)합과 100과의 차이와 n합중 더 작은 쪽을 임시 점수로 선택
        # 만약 합이 같다면 n합을 임시 점수로 선택
        if tmp_sum_n - 100 <= 100 - tmp_sum_n_minus_1:
            tmp_score = tmp_sum_n
        else:
            tmp_score = tmp_sum_n_minus_1
        break
    else:
        tmp_sum_n_minus_1 += list_score[i]
    # 끝까지 먹었지만, 100이 되지 않는다면
    if i == 9:
        # score에 최종합을 넣음
        score = tmp_sum_n

# tmp_score와 score 중 더 큰 값을 max_, 작은 값을 min_에 넣고
max_ = max(tmp_score, score)
min_ = min(tmp_score, score)

# max - 100이 더 작거나 같으면, max_를 score로, 아니면 min_을 score로
if abs(max_ - 100) <= abs(100 - min_):
    score = max_
else:
    score = min_

print(score)

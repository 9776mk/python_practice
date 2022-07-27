N = int(input())
# 전체 사람의 키와 몸무게를 2차원 리스트로 입력받음
list_hw = [list(map(int, input().split())) for _ in range(N)]

# 등수가 들어가는 리스트 초기화
rank_hw = [1 for i in range(N)]

# 순위를 매겨야 함
# 원소 별로 비교를 해서
# 키와 몸무게가 본인보다 큰 사람이 있을 때마다 카운팅을 +1 한다.
# 예시 
# list_hw[0][0] < list_hw[1][0] and list_hw[0][1] < list_hw[1][1] => +1
# 00 10 01 11
# 00 20 01 21
# 00 30 01 31
# 00 40 01 41

# 10 00 11 01
# 10 20 11 21
# 10 30 11 31
# 10 40 11 41

for i in range(N):
    for j in range(N):
        # 본인과 비교를 하면 안되므로 i와 j가 다를 때
        if i != j:
            # 키와 몸무게 둘 다 본인보다 크다면 등수가 하나씩 증가
            if list_hw[i][0] < list_hw[j][0] and list_hw[i][1] < list_hw[j][1]:
                rank_hw[i] += 1
            else:
                continue
        else:
            continue

for i in range(len(rank_hw)):
    print(rank_hw[i], end=' ')

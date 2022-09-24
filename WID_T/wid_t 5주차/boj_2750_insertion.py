# 삽입 정렬
# 왼쪽부분은 정렬되어있다고 가정한 후, 1번째 부터 시작
# 시작하는 인덱스부터 왼쪽과 비교하여 그 값보다 작으면 값을 바꿔줌

N = int(input())
list_ = []

for _ in range(N):
    list_.append(int(input()))

# 삽입 정렬 0번째는 이미 정렬되어 있다고 가정하고 시작
for i in range(1, N):
    # i번째부터 왼쪽으로 진행
    for j in range(i, 0, -1):
        # 만약 왼쪽의 값이 오른쪽의 값보다 더 크면
        if list_[j - 1] > list_[j]:
            # 바꾸기
            list_[j - 1], list_[j] = list_[j], list_[j - 1]

for i in list_:
    print(i)
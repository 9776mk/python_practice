# 선택 정렬
# 가장 큰 수/작은 수를 뽑아서 제일 앞 / 뒤에 집어넣고 범위를 축소
# 남은 부분이 없어질 때까지 반복 진행

N = int(input())
list_ = []

for _ in range(N):
    list_.append(int(input()))

# 0부터 N까지
for i in range(N - 1):
    # 처음 값을 제일 작은 인덱스로 두고
    min_idx = i
    for j in range(i + 1, N):
        # 제일 작은 인덱스 다음부터 끝까지 값들을 비교한 후 제일 작은 값의 인덱스를 찾은 후
        if list_[j] < list_[min_idx]:
            min_idx = j
    # 제일 처음 값과 제일 작은 값의 인덱스 값을 교환
    list_[i], list_[min_idx] = list_[min_idx], list_[i]

    
for i in list_:
    print(i)
# 버블 정렬
# 처음부터 다음 것과 비교해서 더 크면 바꾸고, 아니면 넘어감
# 끝부터 차근차근 정리가 되므로, 인덱스를 하나씩 줄여나감

N = int(input())
list_ = []

for _ in range(N):
    list_.append(int(input()))

for i in range(N-1):
    for j in range(N-i-1):
        if list_[j] > list_[j+1]:
            list_[j], list_[j+1] = list_[j+1], list_[j]
        else:
            continue

for i in list_:
    print(i)
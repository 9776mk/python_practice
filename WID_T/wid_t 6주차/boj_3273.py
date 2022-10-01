# 값들을 입력받음
n = int(input())
list_ = list(map(int, input().split()))
target = int(input())

# 리스트 정렬
list_.sort()
#print(list_)

# 투 포인터 생성
left_ = 0
right_ = n-1

# 값이 일치할 때
cnt = 0

# left_와 right_가 같으면 종료
while left_ != right_:
    # 두 개의 합이 target과 일치하면 cnt+1 해주고, 오른쪽 포인터 왼쪽으로 옮기기
    if list_[left_] + list_[right_] == target:
        cnt += 1
        right_ -= 1
    # 두 개의 합이 target보다 크면 오른쪽 포인터 왼쪽으로 옮기기
    elif list_[left_] + list_[right_] > target:
        right_ -= 1
    # 두 개의 합이 target보다 작으면 왼쪽 포인터 오른쪽으로 옮기기
    elif list_[left_] + list_[right_] < target:
        left_ += 1

print(cnt)
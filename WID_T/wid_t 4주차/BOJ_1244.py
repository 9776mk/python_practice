num_switch = int(input())

list_switch = list(map(int, input().split()))

# 인덱스를 맞춰주기 위해 제일 앞에 숫자 추가
list_ = [0]
for i in list_switch:
    list_.append(i)
#print(list_)

num_student = int(input())

for i in range(num_student):
    a, b = map(int, input().split())
    # 남학생인 경우
    if a == 1:
        i = 1
        i 
        while i*b <= num_switch:
            if list_[i * b] == 1:
                list_[i * b] = 0
            else:
                list_[i * b] = 1
            i += 1
        #print(list_)
    # 여학생인 경우
    else:
        start = b
        end = b
        i = 1
        # 범위를 벗어나지 않을 때
        while b-i > 0 and b + i <= num_switch:
            if list_[b-i] == list_[b+i]:
                start = b - i
                end = b + i
                i += 1
            else:
                break
        # 양쪽 끝 비교
        for i in range(start, end+1):
            if list_[i] == 1:
                list_[i] = 0
            else:
                list_[i] = 1

#print(list_)

for i in range(1, len(list_)):
    print(list_[i], end=' ')
    if i % 20 == 0:
        print()
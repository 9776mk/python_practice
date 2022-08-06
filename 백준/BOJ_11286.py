import sys
import heapq

# 변수 n을 입력 받고
n = int(input())
# heap을 위한 리스트를 생성
heap = []

for i in range(n):
    # x를 입력을 받고
    x = int(sys.stdin.readline())
    # x가 0일때
    if x == 0:
        # heap에서 pop할 수 있으면 
        if heap != []:
            # heap[1]에 있는 수 중 가장 작은 값을 pop
            print(heapq.heappop(heap)[1])
        else:
            # pop을 할 수 없을 경우 0 출력
            print(0)
    # x가 0이 아닐 때면        
    else:
        # heap에 절댓값과 그냥 x를 저장
        heapq.heappush(heap,(abs(x),x))

'''
# 힙을 사용하지 않아 시간 초과
N = int(input())

min_idx = 0

min_abs = 0
list_x = []
list_abs_x = []
list_idx = []

for _ in range(N):
    x_ = int(input())

    min_value = 2**(31)

    # x가 0이 아닐때는 list_x에 추가
    if x_ != 0:
        list_x.append(x_)
        list_abs_x.append(abs(x_))
        cnt = 1

    # x가 0이면
    else:
        # 길이가 0이면 
        if len(list_abs_x)==0 and cnt == 1:
            print(0)
            cnt -= 1
        elif len(list_abs_x)==0 and cnt == 0:
            continue
        # 길이가 0이 아니면
        else:
        # 절댓값이 제일 작은 값을 찾는데
            min_abs = min(list_abs_x)

            # 제일 작은 절댓값이 하나인 경우
            if list_abs_x.count(min_abs) == 1:
                # 
                min_idx = list_abs_x.index(min_abs)
                list_abs_x.pop(min_idx)
                print(list_x.pop(min_idx))

            # 제일 작은 절댓값이 여러개인 경우
            elif list_abs_x.count(min_abs) != 1:

                list_idx = []
                # 작은 값들의 인덱스를 list_idx에 추가하고
                for i in range(len(list_abs_x)):
                    if list_abs_x[i] == min_abs:
                        list_idx.append(i)

                # 인덱스에 있는 값들로 배열에서 찾은 후 값을 비교하여 더 작은 값을 찾은 뒤 출력 및 제거
                for idx_number in list_idx:
                    # min_value 보다 list_x[idx_number]가 더 작을 경우
                    if min_value > list_x[idx_number]:
                        min_value = list_x[idx_number]
                        min_idx = idx_number
                    else:
                        continue
                
                list_abs_x.pop(min_idx)
                print(list_x.pop(min_idx))
                

'''
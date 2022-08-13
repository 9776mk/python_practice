import sys
input = sys.stdin.readline

N = int(input())

list_ = []
set_ = set()
gom_cnt = 0


for i in range(N):
    T = input()
    if T == 'ENTER\n':
        gom_cnt += len(set(list_))
        list_ = []
        continue

    elif i == N-1 and T != 'ENTER\n':
        list_.append(T)
        gom_cnt += len(set(list_))

    else:
        list_.append(T)

print(list_)
print(gom_cnt)


'''
log_list = []


list_=list()
set_ = set()


for log in log_list:

    if log == 'ENTER':
        list_.clear()

    # 닉네임 = log
    # 리스트에서 중복 탐색할 때는 N 만큼의 시간 필요
    # 셋에서 중복 탐색할 때는 1 만큼의 시간이 필요
    else:
        log not is set_:
        set_.add(log)
        gom += 1

'''



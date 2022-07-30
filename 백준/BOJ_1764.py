N, M = map(int, input().split())

not_heard = {}
not_seen = {}

for _ in range(N):
    input_ = input()
    not_heard[input_] = not_heard.get(input_ , 0)

for _ in range(M):
    input_ = input()
    not_seen[input_] = not_seen.get(input_ , 0)


cnt = 0
not_heard_seen = []
for char in not_heard:
    if char in not_seen:
        cnt += 1
        not_heard_seen.append(char)

not_heard_seen.sort()

print(cnt)
for name in not_heard_seen:
    print(name)


'''
# 이름을 키로 사용해서 저장할 딕셔너리 변수
N, M = list(map(int, input().split()))
dict_ = dict()

# N의 크기만큼 듣도 못한 살마을 입력
for i in range(N):
    p = input()
    dict_[p] = '듣도못한'

list_ = []

# M의 크기만큼 보도못한 사람을 입력
for i in range(M):
    p = input()
    # 입력받은 사람이 딕셔너리의 키 중에 있느냐?
    if p in dict_:
        list_.append(p)

list_.sort()
print(len(list_))
for p in list_:
    print(p)









'''












'''
# set과 & 를 이용해서 푸는 풀이
N , M = map(int,input().split())
not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input())
for _ in range(M):
    not_seen.add(input())

not_heard_seen = sorted(list(arr_1 & arr_2))
print(len(not_heard_seen))

for name in not_heard_seen:
    print(name)
'''
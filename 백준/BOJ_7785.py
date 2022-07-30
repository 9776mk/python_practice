N = int(input())

people_ = []
# 이름과 출입을 입력 받음
for _ in range(N):
    name, entry = map(str, input().split())
    # entry가 enter면 people에 추가, leave면 people에서 삭제
    if entry == 'enter':
        people_.append(name)
    if entry == 'leave':
        people_.remove(name)


# 사전 역순으로 정렬
people_.sort(reverse=True)

for person in people_:
    print(person)



'''
N = int(input())
logs = dict()

for i in range(N):
    # 공백으로 나눠진 두 개의 단어
    key, value = input().split()
    logs[ke] vlaue

list_ = []
for key in logs:
    print(key)
    # value 가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == 'enter':
        # 리스트 저장
 
 list_sort(reverse=True)

 for name in list_:
    print(name)




'''
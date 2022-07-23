# 리스트
# 이중 for문. 글자가 같으면 그 글자들의 위치를 기록. 차례대로의 값이 2 이상 차이가 나면 멀리 떨어진 것
# 만약에 다음 글자의 인덱스가 1이상 차이가 나면 cnt에 집어넣는다.
# 문제1. aaabbba에서 index(a)를 할 경우 0만 나옴. -> filter, enumerate 사용한 코드 -> 인덱스를 저장할 수 있는 다른 리스트를 만들어서 해결
# 문제2. 반복되는 문자열은 어떻게 처리할 것인가? -> 문제1에서 구한 index를 사용해 pop한다? -> 인덱스 저장하는 리스트를 활용해 상관이 없었다.

N = int(input())
cnt = 0

for test_case in range(N):
    S = input()
    S1 = list(S)
    is_group = True
    
    for char in S1:
        index_list = []
        for i in range(0,len(S1)):
            if char == S1[i]:
                index_list.append(i)
            else:
                continue

        if len(index_list) != 1:
            for j in range(len(index_list)-1):
                if index_list[j+1] - index_list[j] == 1:
                    continue
                else: # 연속되지 않을 때
                    is_group = False
                    continue
        else:
            continue

    if is_group is True:
        cnt += 1
    else:
        is_group = True

print(cnt)
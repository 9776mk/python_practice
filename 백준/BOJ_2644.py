# 입력을 받고
# DFS를 돌린 후
# True로 바꾸면서 새로운 리스트에 정점들을 리스트로 묶어 추가
# [1,2,3,7,8,9] [4,5,6]

# 두사람이 같은 리스트에 없으면 -1 출력
# [8] [6]은 다른 리스트에 있으므로 -1

# 두 사람이 같은 리스트 안에 있으면 촌수를 계산
# 촌수 계산은 dfs(n1) 에서 cur이 n2가 나올 때까지 하면 될 것 같음
# 두 사람이 같은 리스트에 있는지 확인하기 위해 dfs(n1)를 이미 실행했음.
# dfs(n1) 실행 시 리스트에 cur과 cnt를 저장한 후 인덱스를 받아서 출력?
#   - 딕셔너리 이용?

def dfs(n1):
    # 시작하는 본인은 0촌
    # 시작하는 노드를 스택에 넣고
    stack = [n1]
    # 방문 처리
    visited[n1] = True

    # 스택이 비어 있지 않은 동안
    while stack:
        # stack에서 꺼낸 값을 현재 값으로 설정
        # 부모 노드
        cur = stack.pop()

        # 자식 노드들
        for adj in list_[cur]:
            if not visited[adj]:
                answer[adj] = answer[cur] + 1
                visited[adj] = True
                stack.append(adj)

# 사람 수 n
n = int(input())
# 두 사람 n1, n2 입력
n1, n2 = map(int, input().split())
# 간선 개수 m 입력
m = int(input())

# 각 사람마다 간선을 입력할 간선 리스트 선언
# 1부터 시작하므로 정점 개수 +1
list_ = [[] for _ in range(n+1)]

# 방문을 기록할 리스트 선언
visited = [False] * (n+1)

# 자식 노드
answer = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    list_[a].append(b)
    list_[b].append(a)

# 1. 같은 리스트에 있냐 없냐?
# 2. 같은 리스트에 있으면 촌수가 몇이냐?
#   - 있으면 bfs를 한 번 더 돌려 cur가 n2일 때까지 count를 한 후 count값 출력(x) - 한 번 더 돌리면 안됨

# 같은 리스트에 있는지 검사
# dfs(n1)을 실행한 후 visited[n2]가 True로 바뀌면 같은 연결, False면 다른 연결

dfs(n1)
# print(visited)

# answer가 0이면 방문하지 않은 것이므로
if answer[n2] == 0:
    print(-1)
else:
    print(answer[n2])


# # 연결되지 않은 경우
# if visited[n2] == False:
#     print(-1)
# # 만약 연결되었다면
# else:




'''
def pprint(arr):
    for i in range(len(arr)):
        print(i, arr[i])

n = int(input())
start, end = list(map(int, input().split()))
m = int(input())
# 빈 리스트 (n+1)개르 가진 이차원 리스트
# _ : 값을 사용하지 않음

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 공백을 기준으로 두 개의 숫자가 입력
    x,y = list(map(int, input().split()))
    
    # 무방향 인접 그래프라서
    graph[x].append(y)
    graph[y].append(x)

# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# dfs를 시작하기 위해 기본값 설정
# 스택에 값을 추가할 때 촌수가 같이 추가
# stack = [start]
stack = []
stack.append((start,0))
visited[start] = True

# 정답을 출력할 변수
answer = -1


# 스택이 비어있지 않으면 반복
while len(stack) != 0:
    # LIFO 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()

    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 
    if number == end:
        answer = count
        break


    # 해당하는 값의 인접 그래프 저장
    adj_graph = graph[number]

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수를 같이 append
            stack.append(adj_number, coun + 1)
            # 인접 값을 방문 표시
            visited[adj_number] = True

print(answer)

'''
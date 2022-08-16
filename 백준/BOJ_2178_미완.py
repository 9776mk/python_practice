from pprint import pprint

# 미로 탐색
n, m = map(int, input().split())

# 미로를 입력 받음
miro=[]
for _ in range(n):
    miro.append(list(map(int, input())))

# 미로 방문용 리스트 생성
visited = [[False] * m for _ in range(n)]

# 칸수용 리스트
dist_ = [[0] * m for _ in range(n)]

# 델타 검색
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 좌표 설정
cur = [0, 0]
dist_[cur[0]][cur[1]] = 1
visited[cur[0]][cur[1]] = True

# 스택에 현재 좌표를 집어넣고 
stack = [cur]

while True:
    # 스택이 비어 있지 않으면 반복
    if stack !=[]:
        cur = stack.pop()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            # 인덱스를 벗어나지 않고
            if -1 < nx < n and -1 < ny < m:
                # 마지막 좌표는 방문했더라도 시도해야하므로 미리 조건 설정
                if nx == n-1 and ny == m-1 and dist_[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist_[nx][ny] = dist_[cur[0]][cur[1]] + 1
                    break

                # 마지막 좌표에 이미 깂이 있는 경우
                elif nx == n-1 and ny == m-1 and dist_[nx][ny] != 0:
                    # 현재 마지막 좌표에 있는 값보다 더 작다면
                    if dist_[nx][ny] > dist_[cur[0]][cur[1]] + 1:
                        # 그 값을 마지막 좌표에 넣음
                        dist_[nx][ny] = dist_[cur[0]][cur[1]] + 1
                        break

                # 방문하지 않았을 때
                elif visited[nx][ny] == False:
                    # 방문한 것으로 만들고
                    visited[nx][ny] = True
                    # 만약 그 값이 1이라면
                    if miro[nx][ny] == 1:
                        # 현재까지의 거리에 +1 해서 기록
                        dist_[nx][ny] = dist_[cur[0]][cur[1]] + 1
                        # 만약 새로운 좌표가 도착 좌표라면 그냥 종료후 반복문 다시 실행
                        # 아니라면 현재 좌표를 다음 좌표로 설정
                        stack.append([nx,ny])
                        # print(stack)

    # 도착지와 그 주변을 모두 방문했다면
    elif visited[n-1][m-1] == True and visited[n-2][m-1] == True and  visited[n-1][m-2] == True:
        break

#pprint(visited)
#pprint(dist_)
print(dist_[n-1][m-1])
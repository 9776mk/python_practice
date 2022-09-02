from pprint import pprint
# T = int(input())
T = 1

# ???? cnt 횟수 반영이 안 됨 ????

for test_case in range(T):
    # 가로 길이 M, 세로 길이 N, 배추 위치 K
    #M, N, K = map(int, input().split())
    M, N, K = 5, 3, 6
    # 인접 리스트로 시도? 
 #   bat = [[] for _ in range(K)]
 #   bat = [[0] * M for _ in range(N)]

    # for _ in range(K):
    #     a, b = map(int, input().split())
    #     bat[b][a] = 1
    
    bat = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]

    #pprint(bat)

    # 델타 탐색
    # 위 아래 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문용 리스트 생성
    visited = [[False] * M for _ in range(N)]
    #print(visited)

    # 횟수용 변수
    # dfs가 한 번 실행될 때마다 cnt를 +1씩 해줌
    # dfs가 한 번 실행되는 건 While문이 끝날 때
    cnt = 0

    for x in range(N):
        for y in range(M):
            if bat[x][y] == 0:
                continue

            # 1인 경우 즉, 배추가 있는 경우
            else:
                stack = []
                # 현재 좌표를 방문 처리하고
                stack.append([x,y])
                visited[x][y] = True

                # 스택이 빌 떄까지
                while stack:
                    coor = stack.pop()
                    x_coor = coor[0]
                    y_coor = coor[1]
                # 델타 탐색 진행
                    for i in range(4):
                        nx = x_coor + dx[i]
                        ny = y_coor + dy[i]

                        # 범위를 벗어 나지 않고, 
                        if -1 < nx < N and -1 < ny < M and bat[nx][ny] == 1:
                            # 방문하지 않았다면
                            if visited[nx][ny] == False:
                                stack.append([nx, ny])
                                visited[nx][ny] = True
                
                if stack == []:
                    cnt += 1

    pprint(visited)
    print(cnt)
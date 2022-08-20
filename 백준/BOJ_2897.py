# 지도 입력 받음
# R, C = map(int, input().split())

# map_ = []

# for _ in range(R):
#     list_ = list(map(str, input()))
#     map_.append(list_)

#print(map_)

R = 4
C = 4
map_ = [['#', '.', '.', '#'], ['.', '.', 'X', '.'], ['.', '.', 'X', '.'], ['#', 'X', 'X', '#']]

# 차가 들어갈 곳 델타 탐색
# 차의 크기가 2x2
# [0][0] 부터 [r-1][c-1]까지 위에서부터 아래로 진행하므로 
# 현재 값을 기준으로 우, 우하, 하를 탐색

dx = [0, 1, 1]
dy = [1, 1, 0]

# 주차 공간 횟수 리스트
park_ = [0] * 5

# map 탐색
for i in range(R):
    for j in range(C):
        car_num = 0

        # 만약 현재 좌표가 #, 건물이라면 주차가 불가능하므로 다음 진행
        if map_[i][j] == '#':
            continue

        # 만약 현재 좌표가 X라면, car_num 을 +1 해줌 
        elif map_[i][j] == 'X':
            # 차의 개수 +1 해주고
            car_num = 1

        # 델타 탐색하는데
        for d in range(3):
            nx = i + dx[d]
            ny = j + dy[d]

            # 범위를 벗어나지 않으면 종료
            if not(-1 < nx < R and -1 < ny < R):
                break
                # 만약 빌딩이 있다면 종료
            elif map_[nx][ny] == '#':
                break
                # 만약 차가 또 있다면
            elif map_[nx][ny] == 'X':
                # 차 갯수 추가
                car_num += 1         
        # 델타 탐색을 끝낸 후 차의 개수만큼 해당 인덱스에 1개 추가
        else:
            park_[car_num] += 1

for i in park_:
    print(i)

            


























'''
dr = [0,1,1]
dc = [1,1,0]



building = '#'
car = 'X'
void = '.'

# 숫자가 공백으로 나뉘어져 있는 입력
R, C = list(map(int, input().split()))

list_ = []

# R 줄 만큼의 리스트를 입력
for _ in range(R):
    temp_list = list(input())
    list_.append(temp_list)

break_count_list = [0] * 5


# 이중 반복문 
for r in range(R):
    for c in range(C):

        break_count = 0
        # 조건 1. 기준 좌표가 빌딩(#)이면 안된다.
        if list_[r][c] == building:
            continue
        # 성립이 안되는 조건들은 contionue로 지나가고,
        # 조건이 성립될 때만 정상적인 코드를 실행한다.

        # 조건 2. 기준 좌표가 차라면 부순 횟수 +1
        if list_[r][c] == car:
            break_count += 1


        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]

            # 조건1. 범위를 벗어나면 안된다.
            if not (-1 < nr < R and -1 < nc < C):
                break

            # 조건2. 탐색 좌표에 빌딩이 있으면 안된다.
            if list_[nr][nc] == building:
                break

            # 조건 3. 탐색 좌표에 차가 있으면 부순 횟수를 +1
            if list_[nr][nc] == car:
                break_count += 1

        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)

'''



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
            if (-1 < nr < R and -1 < nc < C):
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
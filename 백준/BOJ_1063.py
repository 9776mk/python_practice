from pprint import pprint

king, stone, n = map(str, input().split())

# king 좌표
king_ =[8-int(king[1]),ord(king[0])-65]
# print(8-int(king[1]), ord(king[0])-65)

# stone 좌표
stone_ = [8-int(stone[1]), ord(stone[0])-65]

com_list = ['R', 'L', 'B', 'T','RT', 'LT', 'RB', 'LB']

# 우 좌 하 상 우상 좌상 우하 좌하
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

# N 번의 명령문을 받음
for _ in range(int(n)):
    com = input()
    # 명령의 종류를 알아내고
    i = com_list.index(com)
    
    # king의 좌표를 옮겼을 때 stone의 좌표와 같은 경우
    if (stone_[0] == king_[0] + dx[i]) and (stone_[1] == king_[1] + dy[i]):
        # stone도 똑같은 시행을 했을 때 범위 안에 있는 경우
        if (-1 < stone_[0]+dx[i] < 8) and (-1 <stone_[1]+dy[i] < 8):
            #stone의 명령 후 좌표가 체스판 범위 안의 경우 stone과 king 둘다 명령 실행
            king_[0] = king_[0] + dx[i] 
            king_[1] = king_[1] + dy[i]
            
            stone_[0] = stone_[0] + dx[i]
            stone_[1] = stone_[1] + dy[i]
    # king의 좌표를 옮겼을 때 stone의 좌표와 다른 경우
    else:
        # king의 명령 후 좌표가 체스판 범위 안인 경우 명령 실행
        if -1 < king_[0]+dx[i] < 8 and -1 < king_[1]+dy[i] < 8:
            # 명령대로 움직임
            king_[0] = king_[0] + dx[i] 
            king_[1] = king_[1] + dy[i]

# 출력은 알파벳, 숫자로 출력되야 함
# 문자열 = 'chr(king_[0]+65)' + '8 - king_[1]'
print(chr(int(king_[1])+65) + str(8-int(king_[0])))
print(chr(int(stone_[1])+65) + str(8-int(stone_[0])))
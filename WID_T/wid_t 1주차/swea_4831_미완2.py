# 한 번에 갈수 있는 정류장 K, 종점의 크기 N, 정류장 개수 M
#K, N, M = 3, 10, 5
K, N, M = 5, 20, 5
#charger = [1,3,5,7,9]
charger = [4, 7, 9, 14, 17]

# 충전 횟수
cnt = 0
# 현재 값
tmp = 0
# 범위를 좁히기 위한 시작 인덱스와 끝 인덱스 선언
tmp_index = 0
# 다음 정류장을 위한 변수
var = 0
# 종료를 위한 변수 설정
end_ = True

# ???? 리스트 범위를 벗어나는 경우를 해결 x ????

while end_:
    # 끝까지 도달 할 수 있으면 종료
    if tmp + K >= N:
        end_ = False
        break
    # 끝까지 도달할 수 없을 때
    else:
        if tmp_index + var < M: ### 리스트 범위를 벗어나는 것을 방지하고자 넣었으나, 이 경우 제일 마지막 경우를 구하지 못하고 종료가 됨
            # 만약 현재 정류장 + K가 다음 정류장 더 크다면
            # 즉 다음 정류장을 가고도 더 갈 수 있는데
            if tmp + K > charger[tmp_index + var]:
                # 끝 인덱스를 하나 더 추가
                var += 1
            # 만약 다음 정류장이 딱 맞아 떨어진다면
            elif tmp + K == charger[tmp_index + var]:
                    tmp = charger[tmp_index + var]
                    tmp_index = tmp_index + var + 1
                    var = 0
                    cnt += 1
            # 만약 다음 정류장에 도착을 못 한다면
            elif tmp + K < charger[tmp_index + var]:
                # 바로 다음 정류장인 경우
                if var == 0:
                    end_ = False
                    cnt = 0
                    break
                else:
                    tmp = charger[tmp_index + var -1]
                    tmp_index = tmp_index + var
                    var = 0
                    cnt += 1
        else:
            break
print(cnt)
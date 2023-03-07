# 시간 초과 O(N^2)
# def solution(k, d):
#     answer = 0

#     for i in range(0, d + 1, k):
#         for j in range(0, d + 1, k):
#             if (i**2) + (j**2) <= (d**2):
#                 answer += 1

#     return answer


def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        for j in range(0, d + 1, k):
            if (i**2) + (j**2) <= (d**2):
                answer += 1

    return answer
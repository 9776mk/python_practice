N, M = map(int, input().split())

# SASA를 만들려면 각각 2개씩 필요
# N, M 중 더 적은 수를 2로 나누면 최댓값이 됨.
print(min(N,M)//2)
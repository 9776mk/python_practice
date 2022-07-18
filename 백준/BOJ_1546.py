N = int(input())
score = list(map(int, input().split()))
new_score = []
M = max(score)

for i in score:
    new_score.append((i/M)*100)

avg_score =  sum(new_score)/N

print(avg_score)
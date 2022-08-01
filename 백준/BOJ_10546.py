import sys

N = int(input())

list_name = []

for i in range(N):
    list_name.append(sys.stdin.readline)

for i in range(N-1):
    list_name.pop(list_name.index(sys.stdin.readline))

print(list_name[0])
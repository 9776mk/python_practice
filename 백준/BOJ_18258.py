from collections import deque
import sys
input = sys.stdin.readline().rstip()

N = int(input())

dq = deque([])

for _ in range(N):
    com = input()
    if 'push' in com:
        num = int(com.split()[1])
        dq.append(num)

    elif com == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
 
    elif com == 'size':
        print(len(dq))
    
    elif com == 'empty':
        if dq:
            print(0)
        else:
            print(1)

    elif com == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif com == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
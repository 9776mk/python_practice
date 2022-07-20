# #은 0,1,2,3,4로 옮겨감
# +는 1. 처음에는 없다가 1,2,3,4로 늘어나는 것 2. 처음에는 4개였다가 3,2,1,0로 줄어드는 것

for i in range(5):
    for j in range(5):
        if(j == i):
            print('#', end='')
        else:
            print('+',end='')
    print()
T = 10

for tc in range(1, T+1):
    a, b = map(str, input().split())
    print(a,b)

    stack_ = []

    for i in b:
        print(i)
        
        if stack_:
            if int(stack_[-1]) == int(i):
                stack_.pop()
            else:
                stack_.append(i)
        else:
            stack_.append(i)
    
    print(stack_)
stick_ = input()

stack_ = []
former_ = ''
cnt = 0

for gual in stick_:
    # 열린 괄호들어오면
    if gual == '(':
        stack_.append(gual)
        former_ = gual
    # 닫힌 괄호들어오면
    else:
        if former_ == '(':
            stack_.pop()
            cnt += len(stack_)
            former_ = gual
            
        else:
            if stack_ != []:
                cnt += 1
            former_ = gual
            stack_.pop()

print(cnt)
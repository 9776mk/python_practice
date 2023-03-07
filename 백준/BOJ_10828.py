N = int(input())

list_ = []

for i in range(N):
    command_ = input()

    if "push" in command_:
        for word in command_.split():
            try:
                list_.append(int(word))
            except ValueError:
                pass

    elif "pop" in command_:
        if len(list_) == 0:
            print(-1)
        else:
            print(list_.pop())

    elif "size" in command_:
        print(len(list_))

    elif "empty" in command_:
        if len(list_) == 0:
            print(1)
        else:
            print(0)

    elif "top" in command_:
        if len(list_) == 0:
            print(-1)
        else:
            print(list_[len(list_) - 1])
def solution(phone_book):
    # 길이를 먼저 정렬한 후 오름차순.
    phone_book.sort(key=len)
    #print(phone_book)

    answer = True
    for i in (0, len(phone_book)-2):
        for j in (i+1, len(phone_book)-1):
            if phone_book[i] in phone_book[j]:
                answer = False
                break
            else:
                continue
    return answer
t = int(input())

for _ in range(3):
    is_anagram = True
    
    A, B = input().split()

    if len(A) != len(B):
        is_anagram = False

    else:
        dict_A = {}
        dict_B = {}

        for a in A:
            dict_A[a] = dict_A.get(a, 0) + 1

        for b in B:
            dict_B[b] = dict_B.get(b, 0) + 1

        # print(dict_A)
        # print(dict_B)

        key_ = list(dict_A.keys())        

        for kb in dict_B.keys():
            # 두 개의 키 값이 다르면
            if kb not in key_:
                # 아나그램 x
                is_anagram = False
            # 두 개의 키 값이 같은데
            else:
                # 둘의 키 값이 다르면
                if dict_A[kb] != dict_B[kb]:
                    is_anagram = False

    if is_anagram :
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')
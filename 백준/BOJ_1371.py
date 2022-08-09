import sys

# read()로 파일을 전부 읽은 후 개행과 띄어쓰기를 전부 없앰
# read로 하기 때문에 vscode에서는 제대로 작동하지 않음
input = sys.stdin.read().replace('\n', '').replace(' ', '')

dict_ = {}
max_list = []

sent_ = input()

for alphabet in sent_:         
    dict_[alphabet] = dict_.get(alphabet, 0) + 1

for k, v in dict_.items():
    if v == max(dict_.values()):
        max_list.append(k)

max_list.sort()

for elem in max_list:
    print(elem, end='')
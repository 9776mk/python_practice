from pprint import pprint

baduk = []

for _ in range(19):
    baduk.append(list(map(int, input().split())))

pprint(baduk) 
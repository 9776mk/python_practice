def make_max(n):
    return int(n.replace('5','6'))

def make_min(n):
    return int(n.replace('6','5'))

A, B = map(str, input().split())

print(make_min(A)+make_min(B), make_max(A) + make_max(B))
# 서로소 집합. 상배집 을 만들기 위한 문제이다.
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ml = list(map(int, input().split()))

    p = [i for i in range(N+1)]

    for i in range(M):
        a, b = ml[i*2], ml[i*2+1]
        union(a, b)

    # union을 다 진행했기 때문에 p 값을 갱신해준다.
    for j in range(1, N+1):
        find_set(j)

    p = set(p[1:])
    print(f"#{tc} {len(p)}")
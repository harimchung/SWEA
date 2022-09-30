def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    return x

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if rank[y] > rank[x]:
        x, y = y, x

    p[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ml = list(map(int, input().split()))

    p = [i for i in range(N+1)]
    rank = [0] * (N+1)

    for i in range(M):
        a, b = ml[i*2], ml[i*2+1]
        union(a, b)


    # union을 다 진행했기 때문에 p 값을 갱신해준다.
    a = set()
    for j in range(1, N+1):
        a.add(find_set(j))

    print(f"#{tc} {len(a)}")
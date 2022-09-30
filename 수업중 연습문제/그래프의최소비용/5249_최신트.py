# 최소신장트리
# kruskal version
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    MST = [0]*(V+1) # 정점의 개수는 V+1개이다.
    adj = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj.append((n1, n2, w))

    adj.sort(key=lambda x:x[2])
    weight = 0
    cnt = 0

    p = [ i for i in range (V+1)]

    while True:
        # 모든 정점에 방문했다면, 방문을 종료한다.
        if cnt == V: # 최소 간선의 개수만큼 골랐다면 종료한다.
            break

        s, e, w = adj.pop(0)
        # 시작점과 종료지점에 대해서 대표가 같다면, continue
        if find_set(s) == find_set(e):
            continue
        else:
            cnt += 1
            union(s,e)
            weight += w

    print(f"#{tc} {weight}")
T = int(input())
INF = 1000
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))

    distance = [INF] * (V+1)
    distance[0] = 0
    U = []
    for _ in range(V):
        u = 0
        minV = INF
        for i in range(V+1):
            if i not in U and distance[i] < minV:
                u = i
                minV = distance[i]

        U.append(u)

        for v in range(len(adj[u])):
            distance[adj[u][v][0]] = min(distance[adj[u][v][0]], minV + adj[u][v][1])
    print(f"#{tc} {distance[V]}")
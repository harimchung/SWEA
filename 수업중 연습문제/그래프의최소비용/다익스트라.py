# 최단 경로를 구하는 과정이다.

def dijkstra(s, V):
    U = [0] * (V+1) # 비용이 결정된 정점을 표시
    U[s] = 1 # 출발점의 비용 결정
    for i in range(V+1):
        D[i] = adjM[s][i]
    # D는 시작점에서 i번쨰 정점으로 가는데 걸리는 가중치의 합이다.

    # 정점의 비용 결정
    for _ in range(V+1):
        u = 0
        minV = INF
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                u = i
        U[u] = 1

        for v in range(V+1):
            if 0 < adjM[u][v] < INF:
                D[v] = min(D[v], D[u] + adjM[u][v])

T = int(input())
for tc in range(1, T+1):
    INF = 10000
    V, E = map(int, input().split())
    adjM = [[INF]*(V+1) for _ in range(V+1)]

    for i in range(V+1):
        adjM[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0]*(V+1)
    dijkstra(0,V)
    print(D)


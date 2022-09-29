def dij(s, V): # s는 시작점, V는 노드의 수
    U = [0] * (V+1) # visited
    U[s] = 1 # 시작지점에 대한 방문처리

    for k in range(V+1):
        D[k] = adjM[s][k] # D[j]는 j까지 이동할 수 있는 거리의 합

    for _ in range(V):
        u = 0
        minV = max_V
        for j in range(V+1):
            if U[j] == 0 and minV > D[j]:
                u = j
                minV = D[j]
        U[u] = 1 # 방문처리

        for l in range(V+1):
            if 0 < adjM[u][l] < max_V:
                D[l] = min(D[l], D[u] + adjM[u][l])


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N은 번호의 끝, E는 구간의 개수
    max_V = 11 # 최대 이동거리가 10 이므로 max 값은 11로 만들었다.
    adjM = [[max_V]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i]= 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w # 방향이 있는 그래프 이기 때문에 한 번만 넣어준다.
    D = [0] * (N+1)
    dij(0, N)
    print(f"#{tc} {D[N]}")
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1) ]
    for _ in range(E):
        s,e,w = map(int, input().split())
        adj[s].append((e,w))

    D = [11]*(N+1) # 최종가중치가 저장될 리스트
    D[0] = 0

    U = [] # 방문처리를 할 리스트

    for _ in range(N):
        u = 0
        minV = 11
        for i in range(N+1):
            if D[i] < minV and i not in U:
                u = i
                minV = D[u]

        U.append(u)

        for j in range(len(adj[u])):
            D[adj[u][j][0]] = min(D[adj[u][j][0]], minV+adj[u][j][1]) # 끝지점

    print(f"#{tc} {D[N]}")
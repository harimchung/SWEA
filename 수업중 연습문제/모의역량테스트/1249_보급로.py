import heapq
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
INF = 1000
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    q = []
    distance = [[INF]*N for _ in range(N)]
    distance[0][0] = 0
    heapq.heappush(q, (0,0,0))

    while q:
        dist, si, sj = heapq.heappop(q)
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]

            if 0 <= ni < N and 0 <= nj < N:

                cost = dist + arr[ni][nj]

                if cost < distance[ni][nj]:
                    distance[ni][nj] = cost
                    heapq.heappush(q, (cost, ni, nj))

    print(f"#{tc} {distance[N-1][N-1]}")
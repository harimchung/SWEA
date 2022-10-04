import heapq

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    fuels = [[100000]*(N) for _ in range(N)]

    q = []
    fuels[0][0] = 0
    heapq.heappush(q, (0, 0, 0))
    find = False
    while q:
        dist, si, sj = heapq.heappop(q)
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]

            if 0 <= ni < N and 0 <= nj < N:
                if fuels[ni][nj] < dist:
                    continue
                cost = dist + 1
                if heights[ni][nj] > heights[si][sj]:
                    cost = cost + heights[ni][nj] - heights[si][sj]

                if cost < fuels[ni][nj]:
                    fuels[ni][nj] = cost
                    heapq.heappush(q, (cost, ni, nj))



    print(f"#{tc} {fuels[N-1][N-1]}")
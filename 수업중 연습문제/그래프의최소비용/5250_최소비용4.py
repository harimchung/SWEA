di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra():
    q = [(0,0)]
    while q:
        now = q.pop(0)
        # 현재 위치로부터 사방탐색을 시작한다.
        for d in range(4):
            ni = now[0] + di[d]
            nj = now[1] + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                height = 0
                if arr[ni][nj] > arr[now[0]][now[1]]:
                    height = arr[ni][nj] - arr[now[0]][now[1]]

                # ni, nj까지 걸리는 연료량 => 현재 + 높이 + 기본
                if fuel[ni][nj] > fuel[now[0]][now[1]] + height + 1:
                    fuel[ni][nj] = fuel[now[0]][now[1]] + height + 1
                    q.append((ni,nj))

T = int(input())
INF = 1000000000
for tc in range(1, T+1):
    N = int(input())

    # 각 위치의 높이를 입력받는다.
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 각 위치까지 갈 때 사용하는 최소 연료
    fuel = [[INF]*N for _ in range (N)]
    fuel[0][0] = 0
    dijkstra()

    print(f"#{tc} {fuel[N-1][N-1]}")

from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(i, j): # s는 시작지점
    q = deque()
    q.append((i,j))
    money[i][j] = 0 # 시작지점의 가격 처리

    while q:
        l = len(q)
        for _ in range(l):
            si, sj = q.popleft()
            for d in range(4):
                ni, nj = si+di[d], sj+dj[d]
                if 0 <= ni < N and 0 <= nj < N :
                    mon = money[si][sj] + 1

                    if hs[ni][nj] > hs[si][sj]:
                        mon += hs[ni][nj] - hs[si][sj]

                    if mon < money[ni][nj]:
                        q.append((ni, nj))
                        money[ni][nj] = mon


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hs = [list(map(int, input().split())) for _ in range(N)]
    money = [[10000]*N for _ in range(N)]
    bfs(0, 0)
    print(f"#{tc} {money[N-1][N-1]}")
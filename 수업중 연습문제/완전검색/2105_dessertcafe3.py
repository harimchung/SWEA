di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]

# 전형적인 dfs 문제이다.
def des(i, j, d): # i,j는 시작하는 좌표의 i,j d는 방향이다.
    global max_V
    if d < 3:
        tmp = d + 2
    else:
        tmp = d + 1
    for k in range(d, tmp):
        ni, nj = i + di[k], j + dj[k]
        if si == ni and sj == nj:
            max_V = max(sum(dessert), max_V)
            return
        if 0 <= ni < N and 0 <= nj < N:
            if not dessert[arr[ni][nj]]:
                dessert[arr[ni][nj]] = 1
                des(ni, nj, k)
                dessert[arr[ni][nj]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_V = -1

    # 탐색을 시작 할 좌표 선택
    for i in range(N - 2):
        for j in range(1, N - 1):
            si, sj = i, j
            dessert = [0]*101
            dessert[arr[si][sj]] = 1
            des(si, sj, 0)

    print(f"#{tc} {max_V}")
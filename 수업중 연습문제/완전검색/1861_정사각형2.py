dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사방탐색하는 함수를 만든다.
def find(i,j):
    global cnt
    global max_cnt
    global max_position

    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == arr[i][j] + 1:
            cnt += 1
            if max_cnt <= cnt:
                if max_cnt == cnt:
                    if max_position > position:
                        max_position = position
                else:
                    max_cnt = cnt
                    max_position = position
            find(ni,nj)

T = int(input())
for tc in range(1, T+1):
    max_position = 1
    max_cnt = 1
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            si, sj = i, j
            cnt = 1
            position = arr[si][sj]
            find(si, sj)
    print(f"#{tc} {max_position} {max_cnt}")


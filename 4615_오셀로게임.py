dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def change(d, i, j, color):
    global cnt_1
    global cnt_2
    global board
    ci, cj = i + dx[d], j + dy[d]
    global temp
    if 0 <= ci < n and 0 <= cj < n:
        if board[ci][cj] == 0:
            return
        elif board[ci][cj] == color:
            if color == 1:
                cnt_1, cnt_2 = cnt_1+temp, cnt_2-temp
            elif color == 2:
                cnt_1, cnt_2 = cnt_1 - temp, cnt_2 + temp
            for k in range(1, temp+1):
                board[ci-k*dx[d]][cj-k*dy[d]] = color
        else:
            temp += 1
            change(d, ci, cj, color)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = list([0]*n for _ in range(n))

    center = n // 2
    board[center][center], board[center-1][center-1] = 2, 2
    board[center-1][center], board[center][center-1] = 1, 1 # 초기상태의 흑, 백 설정
    cnt_1 = 2
    cnt_2 = 2 # 맨 처음 흑, 백 카운트

    for _ in range(m):
        i, j, color = map(int, input().split())
        bi, bj = i-1, j-1

        if color == 1: # 흑돌이 들어온 경우
            cnt_1 += 1
            board[bi][bj] = 1
            # 팔방탐색을 해서 방향을 정한다.
            for d in range(8):
                ni, nj = bi+dx[d], bj+dy[d]
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 2:
                # 그 방향으로 dfs를 진행한다.
                    temp = 0
                    change(d, bi, bj, 1)

        else: # 백돌이 들어온 경우
            cnt_2 += 1
            board[bi][bj] = 2
            # 팔방탐색을 해서 방향을 정한다.
            for d in range(8):
                ni, nj = bi+dx[d], bj+dy[d]
                if 0 <= ni <n and 0 <= nj < n and board[ni][nj] == 1:
                # 그 방향으로 dfs를 진행한다.
                    temp = 0
                    change(d, bi, bj, 2)

    print(f"#{tc} {cnt_1} {cnt_2} ")
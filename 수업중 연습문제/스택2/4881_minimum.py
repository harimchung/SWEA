# 각 줄에 대해서 하나씩 선택하는 함수를 만든다
def select(i, k, tmp):
    global min_V
    if tmp > min_V:
        return

    if i == k:
        min_V = min(min_V, tmp)
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                select(i+1, k, tmp+board[i][j])
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_V = 100
    visited = [0] * N
    select(0, N, 0)

    print(f"#{tc} {min_V}")
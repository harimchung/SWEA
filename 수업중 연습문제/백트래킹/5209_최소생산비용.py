def select(arr, i, k, tmp):
    global min_V

    if i == k:
        if tmp < min_V:
            min_V = tmp
        return

    if tmp > min_V:
        return

    else:
        for j in range(N):
            if not visit[j]:
                visit[j] = 1
                select(arr, i+1, k, tmp+arr[i][j])
                visit[j] = 0 # 원복

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_V = 99*50
    visit = [0] * N
    select(arr, 0, N, 0)
    print(f"#{tc} {min_V}")
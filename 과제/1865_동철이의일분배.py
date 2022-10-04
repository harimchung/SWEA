def backtracking(i, tmp):
    global ans
    if i == n:
        ans = max(ans, tmp)
        return

    if tmp <= ans:
        return

    else:
        for j in range(n):
            if not visit[j]:
                visit[j] = 1
                backtracking(i+1, tmp*(pro[i][j]/100))
                visit[j] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    pro = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    ans = 0
    backtracking(0, 1)
    print(f"#{tc} {ans*100: .6f}")
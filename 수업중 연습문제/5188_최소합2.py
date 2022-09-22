# 누적합과 메모이제이션을 이용해서

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 중간까지 합을 다시 계산하지 않도록
    # 기억해 놓는 방법을 사용한다.
    dp = [[0]*N for _ in range(N)]

    # 이동방향은 왼쪽 => 오른쪽, 위 => 아래
    for i in range(N):
        for j in range(N):
             # 현재 (i,j) 위치에서 위에서도 올 수 있고, 왼쪽에서도 올 수 있을 때
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]
            # 위에서만 올 수 있고, 왼쪽 x
            elif i-1 >=0 and j-1 < 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            # 왼쪽에서만 올 수 있고, 위쪽 x
            elif i-1 <0 and j-1 >= 0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            # 왼쪽도 없고, 위쪽x (시작지점)
            else:
                dp[i][j] = arr[i][j]
    print(f"#{tc} {dp[N-1][N-1]}")


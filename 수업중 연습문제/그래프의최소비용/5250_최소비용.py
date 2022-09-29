# dp로 풀라구 ... 그런다. 다엑스트라? 그걸로는 아무리 해도 모르겠거둥

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hs = [list(map(int, input().split())) for _ in range(N)]
    money = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if 0 <= j-1 < N: # 왼쪽에서 오는 값이 있으면 구한다.
                money1 = money[i][j-1] + 1
                if hs[i][j] > hs[i][j-1]:
                    money1 += hs[i][j] - hs[i][j-1]
                money[i][j] = money1

            if 0 <= i-1 < N:
                money2 = money[i-1][j] + 1
                if hs[i][j] > hs[i-1][j]:
                    money2 += hs[i][j] - hs[i-1][j]

                if money[i][j] > 0:
                    money[i][j] = min(money[i][j], money2)

                else:
                    money[i][j] = money2

    print(f"#{tc} {money[N-1][N-1]}")


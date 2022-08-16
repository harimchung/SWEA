t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    # 다음은 nxn짜리 배열을 board라는 이름의 리스트로 입력받는다.
    board = [list(map(int, input().split())) for _ in range(n)]
    sum_max = 0
    # board에서는 mxm짜리 작은 리스트로 순회해서 더한다.
    for i in range (0, n-m+1):
        for j in range (0, n-m+1):
            sum_box = 0
            # board[i][j] 는 시작점이 되고, 시작점으로부터 mxm짜리 배열을 만들어서 더한다.
            for k in range (0,m):
                for l in range (0,m):
                    sum_box += board[i+k][j+l]
                    if sum_box > sum_max:
                        sum_max = sum_box
    print(f"#{tc} {sum_max}")
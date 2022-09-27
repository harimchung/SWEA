# 행 하나가 증가한다 => 상태공간 트리
# board : 퀸이 놓인 자리
# remain : 남은 퀸 개수
def backtracking(row_num, board, remain):
    global cnt
    if remain == 0:
        cnt += 1
        return
    # 현재 행에서 i번째 열에 퀸을 놓을 수 있는가?
    for i in range(n):
        can_place = True
        # 세로로 퀸이 있는가?
        for j in range(row_num):
            if board[j][i] == 1:
                can_place = False
                break
        # 대각선으로 퀸이 있는가? 다른쪽 대각선으로 퀸이 있는가?
        for j in range(1, row_num+1):
            if 0 <= i-j <n and board[row_num-j][i-j] == 1:
                can_place = False
                break
            elif 0<= i+j < n and board[row_num-j][i+j] == 1:
                can_place = False
                break

        if can_place == True:
            board[row_num][i] = 1
            backtracking(row_num+1, board, remain-1)
            board[row_num][i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    board = [[0]*n for _ in range(n)]
    backtracking(0, board, n)

    print(f"#{tc} {cnt}")
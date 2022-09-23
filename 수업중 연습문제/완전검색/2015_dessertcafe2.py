di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]

def des(i, j, d): #i,j는 현재위치, d는 다음으로 움직일 곳
    global max_V
    dessert[arr[i][j]] = 1  # 우선 방문처리

    if d == 3 and i == si and j == sj:
        max_V = max(max_V, sum(dessert))
        return

    if d == 3:
        if 0 <= i - 1 < N and 0 <= j - 1 < N and dessert[arr[i - 1][j - 1]] == 0:
            des(i + 1, j - 1, 3)
            dessert[arr[i][j]] = 0  # 만약에 더 진행하지 못한다면, 현재 갔던 위치를 0으로 만들고 되돌아오기
            return

    if d == 0:
        if 0 <= i+1 < N and 0 <= j-1 < N and dessert[arr[i+1][j-1]] == 0:
            des(i+1, j-1, 0)    # 더이상 진행하지 못해서 돌아온다면, 위치를 갱신한다.
            i, j = i+1, j-1
            dessert[arr[i][j]] = 0

            des(i, j, 1) # 다음 방향으로 이동한다.
            i, j = i+1, j+1
            dessert[arr[i][j]] = 0

    elif d == 1:
        if 0 <= i+1 < N and 0 <= j+1 < N and dessert[arr[i+1][j+1]] == 0:
            des(i+1, j+1, 1)
            i, j = i+1, j+1
            dessert[arr[i][j]] = 0  # 만약에 더 진행하지 못한다면, 현재 갔던 위치를 0으로 만들고 되돌아오기

            des(i, j, 2) # 다음 방향으로 이동한다.
            i, j = i-1, j+1
            dessert[arr[i][j]] = 0

    elif d == 2:
        if 0 <= i -1 < N and 0 <= j + 1 < N and dessert[arr[i - 1][j + 1]] == 0:
            des(i - 1, j + 1, 2)
            i, j = i-1, j+1
            dessert[arr[i][j]] = 0  # 만약에 더 진행하지 못한다면, 현재 갔던 위치를 0으로 만들고 되돌아오기

            des(i, j, 3)  # 다음 방향으로 이동한다.
            i, j = i-1, j-1
            dessert[arr[i][j]] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_V = -1

    # 탐색을 시작 할 좌표 선택
    for i in range(N - 2):
        for j in range(1, N - 1):
            si, sj = i, j
            dessert = [0]*101
            des(si, sj, 0)

    print(f"#{tc} {max_V}")
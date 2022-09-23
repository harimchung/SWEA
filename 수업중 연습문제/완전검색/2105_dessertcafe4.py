T = int(input())
dr = [1, 1, -1, -1] # 시계방향 탐색
dc = [1, -1, -1, 1]
RD = 0
LD = 1
LU = 2
RU = 3
def travel():
    global max_V
    for d in range(2):



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_V = -1

    for i in range(N):
        for j in range(N):
            start = (i, j)  # 시작위치 기억
            # 내가 먹은 디저트 종류 저장할 배열
            visited = []
            travel(visited, RD, (i,j))

    print(f"#{tc} {max_V}")
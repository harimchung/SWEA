def find_dessert(i, j, len):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탐색을 시작 할 좌표 선택
    for i in range(N-1):
        for j in range(1, N-1):
            si, sj = i, j
            dessert = [arr[si][sj]]
            sd = si + sj
            for nj in range(sj-1, -1, -1):
                ni, nj = sd-nj, nj
                if arr[ni][nj] not in dessert:
                    dessert.append(arr[ni][nj])
                    find_dessert(ni, nj, sj-nj)
                print(dessert)
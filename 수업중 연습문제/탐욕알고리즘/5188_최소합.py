di = [1, 0]
dj = [0, 1]

def f(si, sj, k, temp): # [si,sj]는 시작하는 좌표 위치, k는 반복횟수, temp는 지금까지의 임시합이다.
    global min_V
    if k == (2*N-2):
        if temp < min_V:
            min_V = temp
        return
    if temp > min_V:
        return
    else:
        temp += arr[si][sj]
        for d in range(2):
            ni, nj = si+di[d], sj+dj[d]
            if 0<= ni <N and 0<= nj <N:
                f(ni, nj, k+1, temp)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_V = 10*(2*N)
    f(0, 0, 0, 0)
    print(f"#{tc} {min_V+arr[N-1][N-1]}")
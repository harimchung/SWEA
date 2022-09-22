def p(i, k):
    global min_V
    if i == k:
        temp = 0
        temp += arr[0][pl[0]-1]
        temp += arr[pl[-1]-1][0]
        for j in range(M-1):
            temp += arr[pl[j]-1][pl[j+1]-1]
        if temp < min_V:
            min_V = temp
        return
    else:
        for x in range(M):
            if not used[x]:
                used[x] = 1
                pl[i] = perm[x]
                p(i+1, k)
                used[x] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    perm = [ic for ic in range(2, N+1)]
    M = len(perm)
    used = [0]*M
    pl = [0]*M
    min_V = 100*N

    p(0, M)
    print(f"#{tc} {min_V}")
def nCr(n, r, s): # 리스트에서 순서없이 n개에서 r개를 뽑는 함수
    global min_V
    if r == 0:
        temp = sum(p)
        if temp >= B:
            diff = temp - B
            if diff < min_V:
                min_V = diff
            return
    else:
        for j in range(s, n-r+1):
            p[r-1] = hs[j]
            nCr(n, r-1, j+1)



T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    hs = list(map(int, input().split()))
    hs.sort()
    min_V = 1000000

    for i in range(1, N+1):
        p = [0]*i
        nCr(N, i, 0)
    print(f"#{tc} {min_V}")
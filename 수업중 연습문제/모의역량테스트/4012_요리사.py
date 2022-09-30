# combination1, combination2를 통해서 서로소 집합을 만들었다.
def nCr(n, r, s):
    global min_V
    if r == 0:
        comb2 = []
        for i in range(N):
            if i not in comb:
                comb2.append(i)
        tmp = abs(synergy(comb) - synergy(comb2))
        if tmp < min_V:
            min_V = tmp

    else:
        for i in range(s, n-r+1):
            comb[r-1] = candidates[i]
            nCr(n, r-1, i+1)

def synergy(list):
    cnt = 0
    n = len(list)
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                cnt += ingredients[list[i]][list[j]]
                cnt += ingredients[list[j]][list[i]]
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    candidates = [i for i in range(N)]
    comb = [0] * (N//2)
    min_V = 100000
    nCr(N, N//2, 0)
    print(f"#{tc} {min_V}")
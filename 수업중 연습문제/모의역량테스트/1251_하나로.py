# kruskal 알고리즘으로 풀이

T = int(input())
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(y)] = find_set(x)

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    q = []
    p = [i for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            diff_X, diff_Y = X[j] - X[i], Y[j] - Y[i]
            cost = E * (diff_X**2 + diff_Y**2)
            q.append((cost, i, j))

    q.sort() # 가격이 낮은 순으로 정렬

    cnt = 0
    total_cost = 0

    while True:
        money, start, end = q.pop(0)
        if find_set(start) == find_set(end):
            continue
        union(start, end)
        total_cost += money
        cnt += 1

        if cnt == N-1:
            break

    print(f"#{tc} {round(total_cost)}")






def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]: return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ml = list(map(int, input().split()))
    # n명의 사람에 대해서 m장의 신청서가 제출 되었을 때 만들어 지는 조
    # 일단 n개에 대해서 make-set을 진행한다.
    # ml에 들어오는 순서대로 findset - union을 진행한다.
    p = [0]*(N+1)
    rank = [0]*(N+1)
    for i in range(1, N+1):
        make_set(i)

    for j in range(M):
        a, b = ml[j*2], ml[j*2+1]
        union(a, b)

    print(p)
    p = set(p[1:])
    print(f"#{tc} {len(p)}")

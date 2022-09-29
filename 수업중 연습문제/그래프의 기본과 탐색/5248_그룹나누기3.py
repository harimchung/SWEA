def find_set(x):
    # x가 속한 집합의 대표 찾기
    while x != p[x]:
        x = p[x]
    return x

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    # 두 집합의 대표가 같으면, 합칠 필요가 없다.
    if x == y:
        return

    # x와 y 중에 누구를 대표로 할 것인가?
    # 깊이(rank)가 더 큰 사람을 대표로 할 것이다!
    # 깊이가 깊은 집합을 x라고 하도록 y 집합과 비교
    if rank[y] > rank[x]:
        x, y = y, x
    p[y] = x # 깊이가 깊은 집합이 x가 되도록 처리

    # 두 집합의 깊이가 같다면, x의 깊이를 1 증가 시켜준다.
    if rank[x] == rank[y]:
        rank[x] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))

    # 처음에는 각 집합의 대표가 자기 자신이다.
    p = [i for i in range(N+1)]

    # rank를 통해서 서로소 집합 => 합집합 최적화
    # rank[i] = i번째 집합의 깊이
    # 합집합 시에 깊이가 깊은 집합의 대표를 대표로 정한다.
    rank = [0] * (N+1)

    for j in range(M):
        a, b = pairs[j*2], pairs[j*2+1]
        union(a, b)

    # 각 집합의 대표자가 몇 명인지 구한다 == 집합의 개수
    reps = set()
    for i in range(1, N+1):
        reps.add(find_set(i))
    print(len(reps))
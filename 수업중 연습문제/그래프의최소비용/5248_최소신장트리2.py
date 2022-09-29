# kruskal 알고리즘으로 풀이하기
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
    V, E = map(int, input().split())    # V, E는 각각 노드번호와 간선 개수이다.
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())   # 양끝 노드 n1, n2 가중치 w
        edges.append((w, n1, n2))

    edges.sort() # 가중치를 기준으로 정렬된다.

    # 사이클이 생겼는지 판단하기 위해서 서로소 집합을 사용한다.
    p = [i for i in range(V+1)]
    rank = [0] * (V+1)

    N = V + 1 # N은 정점의 수
    cnt = 0 # cnt는 지금까지 선택한 edges 수
    total = 0 # 가중치의 합

    # kruskal 알고리즘을 진행한다
    # edge를 모두 확인하면서 하나씩 선택 (가중치가 적은 것 부터)
    # 추가하다가 사이클이 생기면, 그 다음 간선을 선택한다.
    for w, s, e in edges:
        # 간선 하나를 뽑아온다 (제일 작은 것 부터)
        # 가져왔는데 s  정점과 e 정점이 같은 집합에 속해있다
        # 즉 사이클이 생긴다 ==> continue
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            total += w
            if cnt == N-1:
                break
    print(f"#{tc} {total}")
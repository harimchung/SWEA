def prim(r, V): # r은 시작지점, V는 총 노드의 개수를 의미한다.
    MST = [0] * (V+1) # MST 포함 여부
    key = [10000] * (V+1)   # 가중치를 최대로 초기화 한다.
    # key[v] => v가 MST에 속한 정점과 연결될 때의 최소 가중치
    key[r] = 0 # 시작지점의 키 값 지정

    for i in range(V):
        u = 0
        minV = 10000
        for j in range(V+1):
            if MST[j] == 0 and key[j] < minV:
                u = j
                minV = key[j]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V, E는 각각 노드번호와 간선 개수이다.
    adjM = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
    for _ in range(E):
        n1, n2, w = map(int, input().split())   # 양끝 노드 n1, n2 가중치 w
        adjM[n1][n2] = w
        adjM[n2][n1] = w

    # Prim 알고리즘을 사용해서 풀이하기
    print(f"#{tc} {prim(0, V)}")

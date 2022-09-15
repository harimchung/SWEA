def binary(node):
    global k
    # 왼쪽이 비어있으면 왼쪽으로 이동
    if 2*node <=n and nodes[2*node] == 0:
        binary(2*node)
    # 자기 자신을 채우고
    nodes[node] = k
    k = k+1
    # 오른쪽으로 이동한다.
    if 2*node+1 <=n and nodes[2*node + 1] == 0:
        binary(2*node+ 1)

T = int(input())
for tc in range(1, T+1):
    k = 1
    n = int(input())
    # 이진 탐색 트리는 중위 순회의 역순으로 넣으면 된다.
    nodes = [0 for _ in range(n+1)]
    binary(1)
    print(f"#{tc} {nodes[1]} {nodes[n//2]}")

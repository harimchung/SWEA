def postorder(node):
    # 만약 노드의 값이 0이면 후위순회를 진행한다.,
    # 현재 노드의 왼쪽 서브트리로 이동한다.
    # 현재 노드의 오른쪽 서브트리로 이동한다.
    pass

T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    nodes= [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        nodes[a] = b

    for k in range(n, 0, -1):
        l_child = 0
        r_child = 0
        if k*2 <= n:
            l_child = nodes[k*2]
        if k*2 + 1 <= n:
            r_child = nodes[k*2+1]
        if nodes[k] == 0:
            nodes[k] = l_child + r_child
    print(f"#{tc} {nodes[l]}")
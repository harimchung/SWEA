from collections import deque

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    nodes = [0]*(2**(2*n-1))
    arr = [list(map(int, input().split())) for _ in range(n)]
    # (0,0) 부터 아래, 오른쪽으로 탐색하면서 tree 배열에 넣는다.
    # 쉽게 생각해 주어진 배열 시계방향으로 45도 틀어보면
    # 보이는 트리를 사용할 것이다.
    que = deque()
    que.append((0,0))
    k = 1
    nodes[k] = arr[0][0]
    while que:
        l = len(que)
        for _ in range(l):
            si, sj = que.popleft()
            for d in [[1,0],[0,1]]:
                    ni, nj = si+d[0], sj+d[1]
                    k += 1
                    if 0 <= ni < n and 0 <= nj < n:
                        que.append((ni, nj))
                        nodes[k] = arr[ni][nj]

print(nodes)




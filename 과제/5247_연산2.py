from collections import deque
def bfs(target, start):
    global cnt
    visited[start] = cnt
    q.append(start)

    while q:
        if visited[target]:     # 목표로 한 곳에 도달하면, 멈춘다.
            break

        else:
            for _ in range(len(q)):
                number = q.popleft()

                n1 = number + 1
                if visited[n1] == 0:
                    visited[n1] = cnt + 1
                    q.append(n1)

                n2 = number - 1
                if n2 > 0 and visited[n2] == 0:
                    visited[n2] = cnt + 1
                    q.append(n2)

                n3 = number * 2
                if visited[n3] == 0:
                    visited[n3] = cnt + 1
                    q.append(n3)

                n4 = number - 10
                if n4 > 0 and visited[n4] == 0:
                    visited[n4] = cnt + 1
                    q.append(n4)

            cnt += 1

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = deque()
    visited = [0]*(10**6+1) # 100만개 만큼의 visit배열을 만들어준다.
    cnt = -1
    bfs(m, n)
    print(f"#{tc} {visited[m]}")
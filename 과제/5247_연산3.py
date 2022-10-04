from collections import deque

def bfs(target, start):
    global cnt
    q.append(start)
    find = False
    while q:
        if find:
            break
        for _ in range(len(q)):
            number = q.popleft()

            if number == target:
                find = True
                break

            else:
                n1 = number + 1
                if not visited[n1]:
                    visited[n1] = 1
                    q.append(n1)

                n2 = number -1
                if n2 > 0 and not visited[n2]:
                    visited[n2] = 1
                    q.append(n2)

                n3 = number*2
                if not visited[n3]:
                    visited[n3] = 1
                    q.append(n3)

                n4 = number-10
                if n4 > 0 and not visited[n4]:
                    visited[n4] = 1
                    q.append(n4)
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = deque()
    visited = [0]*(10**6+1)
    cnt = -1
    bfs(m, n)
    print(f"#{tc} {cnt}")

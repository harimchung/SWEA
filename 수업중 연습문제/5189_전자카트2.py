T = int(input())

def patrol(now, e_sum):
    global min_V
    # 최적화를 위한 조건 (현재의 합이 내가 알고 있는 최소값보다 크면, 더이상 실행할 필요가 없다.)
    if e_sum > min_V:
        return

    if 0 not in visited:
        min_V = min(min_V, e_sum + e[now][0])
        return

    # 현재 위치에서 다음으로 갈 수 있는 방 탐색
    for next_room in range(N):
        if next_room != now and visited[next_room] == 0:
            # 다음 방을 갔다고 체크하고 길을 찾는다.
            visited[next_room] = 1
            # 합을 최신화 한 후, 재귀 호출
            patrol(next_room, e_sum + e[now][next_room])
            # 방문체크 해제
            visited[next_room] = 0

for tc in range(1, T+1):
    N = int(input())

    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    # 처음 방은 출발 이후에 돌아올 수 없다!
    visited[0] = 1

    min_V = 10000
    patrol(0, 0)
    print(f"#{tc} {min_V}")
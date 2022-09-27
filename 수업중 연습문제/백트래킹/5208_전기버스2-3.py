T = int(input())

def backtracking(idx, cnt):
    global min_v

    if idx >= N-1:
        min_v = min(min_v, cnt)
        return
    if cnt >= min_v:
        return

    for i in range(1, bus_stop[idx]+1):
        backtracking(idx+i, cnt+1)

for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    N = bus_stop.pop(0)
    min_v = 101

    backtracking(0, -1)
    print(f"#{tc} {min_v}")
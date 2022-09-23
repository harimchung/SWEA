T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = []
    for _ in range(N):
        s, e = map(int, input().split())
        times.append((s,e))
    times = sorted(times, key=lambda x:(x[1], x[0]))

    select = []
    for i in range(N):
        if not select:
            select.append(times[i])
            continue
        end = select[-1][1]
        if times[i][0] >= end:
            select.append(times[i])
    print(f"#{tc} {len(select)}")

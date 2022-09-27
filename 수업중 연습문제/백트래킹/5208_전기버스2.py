T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    N = num_list.pop(0)

    cnt = 0
    target_idx = N-1 # N-1 혹은 그 이상에 도착하면 반복문을 중단한다.

    i = 0
    now_possible = num_list[i]
    while True:
        if i + now_possible >= target_idx:
            break

        max_V = 0
        max_i = 0

        for k in range(i+1, i+now_possible+1):
            temp = k + num_list[k]
            if temp >= max_V:
                max_V = temp
                max_i = k

        i = max_i
        now_possible = num_list[max_i]
        cnt += 1
    print(f"#{tc} {cnt}")
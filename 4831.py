# t는 노선의 개수 (즉, 총 반복해야 하는 테스트 케이스가 담긴 수 이다.)
t = int(input())
for test_case_num in range(1, t+1):
    k, n, m = map(int, (input()).split())
    station_list = list(map(int, input().split()))
    m_list = [0]*(n+1)
    for _ in station_list:
        m_list[_] = 1

    initial_k = k
    position = 0
    cnt = 0

    while position <= n:
        if position + k >= n:
            break
        if m_list[position + k] == 0:
            k = k-1
            if k == 0:
                cnt = 0
                break
        elif m_list[position + k] == 1:
            position = position + k
            cnt += 1
            k = initial_k
    print(f"#{test_case_num} {cnt}")







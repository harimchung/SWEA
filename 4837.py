A = [1, 2, 3, 4, 5, 6, 7,  8, 9, 10, 11, 12]
n = len(A)
T = int(input())
for tc in range (1, T+1):
    cnt = 0
    len_sub, want_sum = map(int, input().split())
    for i in range(1<<n):
        sum = 0
        sum_cnt = 0
        for j in range(n):
            if i & (1<<j):
                sum += A[j]
                sum_cnt += 1

        if sum_cnt == len_sub and sum == want_sum:
            cnt += 1

    print(f"#{tc} {cnt}")

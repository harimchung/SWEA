# 카드를 교환한 횟수를 기록할 cnt
def card_swap(cnt):
    global max_val
    if cnt == N:
        num = int("".join(S))
        max_val = max(max_val, num)
        return

    else:
        for i in range(len(S)-1):
            for j in range(i+1, len(S)):
                S[i], S[j] = S[j], S[i]
                card_swap(cnt+1)
                S[i], S[j] = S[j], S[i]

T = int(input())

for tc in range(1, T+1):
    S, N = input().split()

    S = list(S)
    N = int(N)

    # 주어진 교환 횟수가 카드의 자리수보다 크면, 의미가 없다.
    if N > len(S):
        N = len(S)

    # 최대 값
    max_val = 0
    card_swap(0)
    print(f"#{tc} {max_val}")
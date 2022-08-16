T = int(input())
for tc in range(1, T+1):
    # n은 당근의 개수(리스트 길이), c는 각 당근의 크기가 주어진다.
    n = int(input())
    c = list(map(int, input().split()))

    bigger = 1
    max = 1
    for i in range(1, n):
        if c[i] == c[i-1] + 1 :
            bigger += 1
        else :
            bigger = 1
        if bigger > max:
            max = bigger
    print(f"#{tc} {max}")

# 이진탐색
T = int(input())
for tc in range(1, T+1):
    # 각 테스트케이스 별로 p, pa, pb가 각각주어진다.
    p, pa, pb = map(int, input().split())
    l = 1
    r = p
    c = int((l+r)/2)

    # A의 탐색하는 숫자를 검색한다.
    cnt_a = 1
    while c != pa:
        if pa > c:
            l = c
        else :
            r = c
        c = int((l + r) / 2)
        cnt_a += 1

    l = 1
    r = p
    c = int((l+r)/2)
    # B의 탐색하는 회수를 찾는다.
    cnt_b = 1
    while c != pb:
        if pb > c:
            l = c
        else:
            r = c
        c = int((l + r) / 2)
        cnt_b += 1

    if cnt_a < cnt_b :
        winner = "A"
    elif cnt_a > cnt_b:
        winner = "B"
    else:
        winner = "0"
    print(f"#{tc} {winner}")
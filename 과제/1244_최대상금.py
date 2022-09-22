def c(m, cnt):
    global ans
    if cnt == m:
        num = ''.join(cl)
        if num > ans:
            ans = num
        return
    else:
        for i in range(n):
            for j in range(i + 1, n):
                cl[i], cl[j] = cl[j], cl[i]
                temp = ''.join(cl)
                if not temp in tl[cnt]:
                    tl[cnt].append(temp)
                    c(m, cnt + 1)
                cl[i], cl[j] = cl[j], cl[i]


T = int(input())
for tc in range(1, T + 1):
    cards, m = input().split()
    cl = [card for card in cards]
    m = int(m)  # m은 교환횟수
    n = len(cl)
    ans = '000000'
    tl = [[] for _ in range(m+1)]
    c(m, 0)
    print(f"#{tc} {ans}")
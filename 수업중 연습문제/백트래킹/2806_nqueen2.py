def queen(i, k):
    global cnt
    if i == k:
        cnt += 1
        return
    else:
        for j in range(n):
            if not visit[j]:
                visit[j] = 1
                if possible(i, j):
                    queen(i+1, k)
                visit[j] = 0

def possible(i, j):
    if not nl:
        nl.append((i,j))
        return True
    else :
        for q in range(len(nl)):
            si, sj = nl[q]
            if i+j == si+sj : # 같은 대각선에 있을 수 없다.
                return False
            elif sj-si == j-i:
                return False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    visit = [0]*n
    nl = []
    queen(0, n)
    print(f"#{tc} {cnt}")
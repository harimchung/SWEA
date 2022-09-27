# n-queen
def queen(i, k):
    global cnt
    if i == k:
        cnt += 1
        return
    else:
        for j in range(n):
            if not visit[i][j]: # 방문하지 않은 경우, 유효성 검사를 실시한다.
                if possible(i, j):
                    visit[i][j] = 1
                    queen(i+1, k)
                    visit[i][j] = 0

def possible(i,j):
    # 유효성 검사를 진행하는 함수
    # 가능할 경우 => True
    # 불가능할 경우 => False 를 반환합니다.
    # nl(가능한 숫자 집합이 비었을 때)
    if not nl:
        nl.append((i,j))
        return True

    else: # 가능한 숫자 집합이 비어있을 때
        m = len(nl)
        for q in range(m):
            si, sj = nl[q]
            if si == i: # 같은 열에 있을 수 없다.
                return False
            elif i+j == si+sj : # 같은 대각선에 있을 수 없다.
                return False
            elif sj-si == j-i:
                return False

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    visit = [[0]*n for _ in range(n)]
    nl = []
    queen(0, n)
    print(f"#{tc} {cnt}")
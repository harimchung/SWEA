def bruteforce(p, t):
    ti = 0 # 전체 텍스트의 인덱스 (비교위치)
    pi = 0 # 패턴 인덱스 (비교 위치)
    tl = len(t)
    pl = len(p)

    count = 0 # 패턴 일치 회수

    while pi < pl and ti < tl:
        if t[ti] != p[pi]:
            ti = ti - pi
            pi = -1
        ti += 1
        pi += 1

        if pi == pl : # 패턴 인덱스가 패턴 길이만큼 가면, 일치하는 패턴을 찾았다.
            count += 1
            pi = 0 # 다음 탐색을 위해서 패턴 위치를 조정한다.
            ti += 1
    return count

T = 10
for tc in range (1, T+1):
    n = int(input())
    p = input()
    t = input()

    answer = bruteforce(p,t)
    print(f"#{tc} {answer}")

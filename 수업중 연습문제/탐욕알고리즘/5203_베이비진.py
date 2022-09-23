def tri(cnt_list):
    for k in range(10):
        if cnt_list[k] >= 3:
            return 1
    return 0

def run2(cnt_list):
    for l in range(8):
        if cnt_list[l] and cnt_list[l+1] and cnt_list[l+2]:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    p1, p2 = [0] * 6, [0] * 6
    p1_cnt, p2_cnt = [0] * 10, [0] * 10
    winner = 0

    for i in range(6):
        p1[i] = cards[i*2]
        p1_cnt[p1[i]] += 1

        p2[i] = cards[i*2 + 1]
        p2_cnt[p2[i]] += 1

        # 3번 나누고 부터 검사를 시작한다.
        if i < 3: continue

        a = tri(p1_cnt) + run2(p1_cnt)   # 둘 중에 하나만 해당해도 값은 1 이상이다
        b = tri(p2_cnt) + run2(p2_cnt)   # 둘 중 하나만 해당해도 값은 1 이상이다

        # 만약 a, b 둘다 0 이라면 해당사항이 없으므로 다음으로 분배한다.
        if a+b == 0: continue

        # a의 값이 0이아니라면, 승자는 무조건 1이된다.
        elif a != 0:
            winner = 1
            break

        # a의 값이 0이고(즉 1이 베이비진이 아니고) b는 0이 아니라면 승자는 2가 된다.
        elif a == 0 and b != 0:
            winner = 2
            break

    # 모두 다 분배했는데도 승자가 없다면, 무승부 이므로 winner는 처음 설정한대로 0이 된다.

    print(f"#{tc} {winner}")


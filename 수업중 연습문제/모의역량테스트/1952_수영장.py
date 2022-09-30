def three_month(money_list, i, j, k):
    tmp1, tmp2, tmp3 = 0, 0, 0
    for m in range(3):
        tmp1 += money_list[i+m]
        tmp2 += money_list[j+m]
        tmp3 += money_list[k+m]
    return sum(money_list) + three * 3 - (tmp1+tmp2+tmp3)

def two_month(money_list, i, j):
    tmp1, tmp2 = 0, 0
    for m in range(3):
        tmp1 += money_list[i+m]
        tmp2 += money_list[j+m]
    return sum(money_list) + three*2 - (tmp1+tmp2)

def one_month(money_list, i):
    tmp1 = 0
    for m in range(3):
        tmp1 += money_list[i+m]
    return sum(money_list) + three - tmp1

T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))
    money = [0]*12

    # 일권/ 월권 중에 월권이 싸지는 분기점(limit)을 구해서
    # 일단 money에는 일권/월권중에 싼 값을 택할 수 있게 만든다.
    limit = month/day
    for i in range(12):
        if plan[i] > limit:
            money[i] = month
        else:
            money[i] = day*plan[i]

    # 1. 일권 + 월권의 합
    min_V = sum(money)

    # 2. 연간 권의 합
    if year < min_V:
        min_V = year

    # 3. 3개월 권의 합

    # 3-1. 3개월씩 4번 끊는 경우
    if three*4 < min_V:
        min_V = three*4

    # 3-2. 3개월씩 3번 끊는 경우
    for i in range(0, 10):
        for j in range(i+3, 10):
            for k in range(j+3, 10):
                if three_month(money, i, j, k) < min_V:
                    min_V = three_month(money, i, j, k)

    # 3-3. 3개월씩 2번 끊는 경우
    for i in range(0, 10):
        for j in range(i+3, 10):
            if two_month(money, i, j) < min_V:
                min_V = two_month(money,i,j)

    # 3-4. 3개월씩 1번 끊는 경우
    for i in range(0, 10):
        if one_month(money, i) < min_V:
            min_V = one_month(money,i)

    print(f"#{tc} {min_V}")
def perm(j, k):
    global min_V, max_V, cnt
    if j == k:
        cnt += 1
        # temp = add(perm_result)
        # if temp < min_V:
        #     min_V = temp
        # if temp > max_V:
        #     max_V = temp
        return
    else:
        for i in range(4):
            if symbol_cnt[i] > 0:
                symbol_cnt[i] -= 1
                perm_result[j] = symbol[i]
                perm(j+1, k)
                symbol_cnt[i] += 1

def add(list):
    tmp = numbers[0]
    for i in range(N-1):
        if list[i] == "+":
            tmp += numbers[i+1]
        elif list[i] == "-":
            tmp -= numbers[i+1]
        elif list[i] == "*":
            tmp *= numbers[i+1]
        else:
            tmp = int(tmp / numbers[i+1])
    return tmp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    symbol_cnt = list(map(int, input().split()))
    symbol = ["+", "-", "*", "/"]
    numbers = list(map(int, input().split()))

    min_V = 10**8
    max_V = -10**8

    cnt = 0
    perm_result = [0]*(N-1)
    perm(0, N-1)

    print(f"#{tc} {cnt}")
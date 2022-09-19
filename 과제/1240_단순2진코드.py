code = {
    "0001101":0, "0011001":1, "0010011":2,
    "0111101":3, "0100011":4, "0110001":5,
    "0101111":6, "0111011":7, "0110111":8,
    "0001011":9
}

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]


    new_line = []
    # 줄 선택
    flag = True
    for i in range(0, m):
        row = arr[i]
        for k in range(len(row)-1, -1, -1):
            if arr[i][k] == 1:
                for j in range(k-55, k+1):
                    new_line.append(arr[i][j])

                flag = False
                break
        if not flag:
            break


    temp = 0
    ans = 0
    # 줄에서 탐색


    for k in range(0, 50, 7):
        want_key = ""
        for j in range(7):
            want_key += str(new_line[k+j])

        if k % 2 == 0:
            temp += code[want_key] *3
            ans += code[want_key]
        else:
            temp += code[want_key]
            ans += code[want_key]


    if temp % 10 != 0:
        ans = 0
    print(f"#{tc} {ans}")
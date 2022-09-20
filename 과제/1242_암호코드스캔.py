# import sys
# sys.stdin = open("password.txt")
codes = {
    (3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}


def binary(number):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if number & (1 << j) else "0"
    return output


T = int(input().strip())
for tc in range(1, T + 1):
    n, m = map(int, input().strip().split())
    # set을 이용해서 중복제거
    arr = list(set([input() for _ in range(n)]))
    # 0만 있는 배열 제거
    arr = sorted(arr)[1:]

    # 16진수를 2진수로 변환
    l = len(arr)
    for i in range(l):
        row = arr[i]
        ans = ""
        for j in range(m):
            ans += binary(int(row[j], 16))
        arr[i] = ans


    # 처음으로 만나는 1 찾기
    for k in range(l):
        row = arr[k]
        for x in range(4*m-1, -1, -1):
            # 제일 처음부터 역수로
            if row[x] == "1":
                start_x = x
                break

        c1, c2, c3, c4 = 0, 0, 0, 0
        for y in range(start_x, -1, -1):
            if 
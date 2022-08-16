T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(input())
    max = 0

    for i in range(1, n):
        a[i] = int(a[i - 1]) * int(a[i]) + int(a[i])

    for j in a:
        if int(j) > max:
            max = j

    print(f"#{tc} {max}")
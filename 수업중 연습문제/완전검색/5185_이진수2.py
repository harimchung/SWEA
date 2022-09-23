def binary(n):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if n & (1<<j) else "0"
    return output

T = int(input())
for tc in range(1, T+1):
    n, m = input().split()
    n = int(n)
    ans = ""
    for number in m:
        number = int(number, 16)
        ans += binary(number)
    print(f"#{tc} {ans}")

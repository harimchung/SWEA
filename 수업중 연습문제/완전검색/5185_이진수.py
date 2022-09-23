alphabet = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
def binary(number):
    global ans
    if number == 0:
        return

    if number == 1:
        ans += "1"

    else:
        ans += str(number%2)
        binary(number//2)

T = int(input())
for tc in range(1, T+1):
    n, num = input().split()
    n = int(n)
    final_ans = ""
    for i in range(n):
        ans = ""
        number = num[i]
        if "0" <= number <= "9":
            binary(int(number))
            while len(ans) < 4:
                ans += "0"

        else:
            binary(alphabet[number])
        ans = ans[::-1]
        final_ans += ans
    print(f"#{tc} {final_ans}")

# 1
# 4 07FE

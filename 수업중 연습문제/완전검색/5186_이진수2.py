T = int(input())
for tc in range(1, T+1):
    number = float(input())
    binary_num = ""
    for i in range(1, 13):
        if number == 0:
            break
        if number >= 2**(-i):
            binary_num += "1"
            number -= 2**(-i)
        else :
            binary_num += "0"
    if number != 0:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {binary_num}")

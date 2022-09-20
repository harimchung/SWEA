def binary(n):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if n & (1<<j) else "0"
    return output

m = "1E06079861E79F99FE079861E79F8"
ans=""
for number in m:
    number = int(number, 16)
    ans += binary(number)
print(ans)
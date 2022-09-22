# def binary(n):
#     output = ""
#     for j in range(3, -1, -1):
#         output += "1" if n & (1<<j) else "0"
#     return output
#
# m = "1E06079861E79F99FE079861E79F8"
# ans=""
# for number in m:
#     number = int(number, 16)
#     ans += binary(number)
# print(ans)
# N = 3
# perm = [i for i in range(2, N+1)]
# M = len(perm)
# pl = [0]*M
# pl.insert(0, 1)
# pl.insert(N, 1)
# print(pl)

a = [1,2,3,4,5]
a.extend([0]*3)
print(a)
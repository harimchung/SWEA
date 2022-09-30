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

# a = [1,2,3,4,5,6]
#
# def three_month(money_list, i, j, k):
#     tmp1, tmp2, tmp3 = 0, 0, 0
#     for m in range(3):
#         tmp1 +=money_list[i+m]
#         tmp2 +=  money_list[j+m]
#         tmp3 += money_list[k+m]
#     return sum(money_list) + three * 3 - (tmp1+tmp2+tmp3)
#
# three = 10
# money = [0, 18, 16, 16, 19, 19, 18, 18, 15, 16, 17, 16]
#
# for i in range(0, 10):
#     for j in range(i + 3, 10):
#         for k in range(j + 3, 10):
#             print(three_month(money, i, j, k))

# def nCr(n,r,s):
#     # combination n개에서 r개 뽑는방법, s는 시작지점
#     # 조합의 기본 성질인 nCr = n-1Cr-1 + nCr-1 임을 이용한다.
#
#     if r == 0:
#         print(*comb)
#
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = N[i]
#             nCr(n, r-1, i+1)
# n = 5
# N = [i for i in range(1, n+1)]
# r = 3
# comb = [0] * r
# nCr(n, r, 0)


# def combination(n,r,s):
#     # n개에서 r개를 고르는 경우, s는 시작점의 번호
#     if r == 0: # 더이상 고를 것이 없을 때,
#         print(*comb)
#
#     else:
#         for i in range(s, n-r+1): # 시작점에서부터 n-r번까지 중에서 고를 수 있다.
#             comb[r-1] = N[i] # combination의 마지막부터 채워넣는다.
#             combination(n, r-1, i+1) # 1개를 뽑았기 때문에 다음으로 뽑을 것은 n개중에서 r-1개를 뽑는 것. i다음부터 뽑을 수 있다.
# n = 7
# N = [i for i in range(1, n+1)]
# r = 2
# comb = [0]*r
# combination(n,r,0)

# def nCr(n,r,s):
#     if r == 0:
#         print(*comb)
#
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = N[i]
#             nCr(n, r-1, i+1)
#
# n = 5
# N = [ i for i in range(1, n+1)]
# r = 3
# comb = [0] * r
# nCr(n,r,0)

# a = [1,2,3,4,5]
# n = len(a)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i&(1<<j):
#             print(a[j], end=" ")
#     print()

# 개수가 2개, 개수가 3개인 부분집합 만들기
# from itertools import combinations
# arr = [1,2,3]
#
# print(list(combinations(arr, 1)))

print(-1/3)
print(int(-2/3)+7+9)
print(2/3)
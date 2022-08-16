# a = list(map(int, input().split()))
# n = 500000
# l = len(a)
# for i in range(0, n+1):
#     min_Idx = i
#     for j in range(i+1, l):
#         if a[j] < a[min_Idx]:
#             min_Idx = j
#     a[i], a[min_Idx] = a[min_Idx], a[i]
# print(a[n])

a = list(map(int, input().split()))
a.sort()
print(a)
# n = len(a)
# for i in range (n-1, 0, -1):
#     for j in range (0, i):
#         if a[j+1] > a[j]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)
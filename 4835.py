# # T는 테스트케이스의 개수
# T = int(input())
#
# for _ in range(1,T+1):
#     N, M = map(int, input().split())
#     ai = list(map(int, input().split()))
#     sum_list = []
#
#     for i in range(0, N-M+1):
#         sum = 0
#         for j in range(i, i+M):
#             sum += ai[j]
#         sum_list.append(sum)
#
#     max = sum_list[0]
#     for sum_max in sum_list:
#         if sum_max > max:
#             max = sum_max
#
#     min = sum_list[0]
#     for sum_min in sum_list:
#         if sum_min < min:
#             min = sum_min
#
#     print(f"#{_} {max-min}")

# append 쓰지 않고 다시 풀이하기
# T는 테스트케이스의 개수
T = int(input())

for _ in range(1,T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    max_sum = 0
    min_sum = 10000*99

    for i in range(0, N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += ai[j]

        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum

    print(f"#{_} {max_sum-min_sum}")
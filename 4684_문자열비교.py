# #1 brute force 방법으로 검색하기
# T = int(input())
# for tc in range (1, T+1):
#     str1 = input()
#     str2 = input()
#
#     n = len(str1)
#     m = len(str2)
#
#     # str1을 순회할 index를 i, str2를 순회할 index를 j라고 한다.
#     i = 0
#     j = 0
#     in_text = 0
#     # 브루트 포스를 이용해서 str2의 요소가 전부 다 돌때까지 구한다.
#     while j < m:
#         # 만약 i번째 str1과, str2의 j번째 요소가 같으면,
#         if str1[i] == str2[j]:
#             i += 1
#         else:
#             i = 0
#         j += 1
#
#         if i == n:
#             in_text = 1
#             break
#
#     print(f"#{tc} {in_text}")

# in 을 사용해서 검색하기
# T = int(input())
# for tc in range (1, T+1):
#     str1 = input()
#     str2 = input()
#     in_text = 0
#     if str1 in str2:
#         in_text = 1
#     print(f"#{tc} {in_text}")

# brute force (교과서 버전)
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    n = len(str1)
    m = len(str2)

    i = 0
    j = 0
    in_text = 0
    while i < n and j < m:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
        if i == n:
            in_text = 1

    print(f"#{tc} {in_text}")
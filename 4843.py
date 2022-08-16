# 특별한 정렬
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     a = list(map(int, input().split()))
#
#
#     for i in range (n-1):
#         min_idx = i
#         for j in range (i+1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#
#     print(f"#{tc}", end=" ")
#
#     for i in range(5):
#         print(a[-(i + 1)], end=" ")
#         print(a[i], end=" ")
#     print()

# max 와 min을 모두 선택정렬로 찾기
T = int(input())
for tc in range (1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    # max idx 찾기
    for i in range (n-1, 0, -1):
        max_idx = i
        for j in range(0, i):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

    print(f"#{tc}", end=" ")
    print(a)

# 교수님의 풀이
T = int(input())
for tc in range (1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    index = 0 # 바꿀 원소의 인덱스 (최대값 or 최소값)
    i = 0 # 탐색을 시작할 위치

    for ni in range(10):
        # 10번 반복한다.
        for j in range(i, n) : # 최대값 혹은 최소값을 찾기 시작한다.
            if ni % 2==0 and numbers[j] > numbers[index]:
                # 최대값의 인덱스
                index = j
            if ni % 2==1 and numbers[j] > numbers[index]:
                # 최소값의 인덱스
                index = j
            i += 1 # 다음에 와야할 원소의 위치를 증가
            # 현재 위치와 최대값. 최소값의 위치에 있는 원소를 자리 바꿔주기
            numbers[ni], numbers[index] = numbers[index], numbers[ni]

    print(f"#{tc}", end = " ")
    for i in range(10):
        print(f"{numbers[i]}", end=" ")
    print()
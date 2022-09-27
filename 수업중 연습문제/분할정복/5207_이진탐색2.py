T = int(input())
R = 1
L = 2
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split())) # 정렬대상
    B = list(map(int, input().split())) # 검색 대상

    A.sort()
    cnt = 0
    for number in B:
        left = 0
        right = N-1
        dir = -1 # 처음 시작할 때에는 방향이 없는 상태이다

        while left <= right:
            mid = (left+right) // 2
            if A[mid] == number:
                cnt += 1
                break

            elif A[mid] > number:
                right = mid - 1
                # 이전에 선택한 범위가 왼쪽이면 조건 위반이다.
                if dir == L:
                    break
                dir = L

            elif A[mid] < number:
                left = mid + 1
                if dir == R:
                    break
                dir = R

    print(f"#{tc} {cnt}")

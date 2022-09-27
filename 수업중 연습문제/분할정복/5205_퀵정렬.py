def quick(arr, s, e): # 퀵정렬은 정렬을 하고 싶은 배열, 시작점, 끝 점이 주어진다.
    if s >= e:
        return  # 원소가 1개인 경우 리턴
    pivot = s # 피벗은 배열의 첫 원소로 지정한다.
    left, right = s+1, e # 피벗을 제외한 좌, 우 상한 하한선을 지정한다.

    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복한다.
        while left <= e and arr[left] <= arr[pivot]:
            left += 1
        while right > s and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick(arr, s, right-1)
    quick(arr, right+1, e)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    quick(nl, 0, N-1)
    print(f"#{tc} {nl[N//2]}")

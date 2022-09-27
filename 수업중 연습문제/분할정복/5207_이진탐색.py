import sys
# def quick(arr, s, e): # 퀵정렬은 정렬을 하고 싶은 배열, 시작점, 끝 점이 주어진다.
#     if s >= e:
#         return  # 원소가 1개인 경우 리턴
#     pivot = s # 피벗은 배열의 첫 원소로 지정한다.
#     left, right = s+1, e # 피벗을 제외한 좌, 우 상한 하한선을 지정한다.
#
#     while left <= right:
#         # 피벗보다 작은 데이터를 찾을 때까지 반복한다.
#         while left <= e and arr[left] <= arr[pivot]:
#             left += 1
#         while right > s and arr[right] >= arr[pivot]:
#             right -= 1
#         if left > right:
#             arr[right], arr[pivot] = arr[pivot], arr[right]
#         else:
#             arr[right], arr[left] = arr[left], arr[right]
#
#     quick(arr, s, right-1)
#     quick(arr, right+1, e)

def binarySearch(s, e, target, direction): # 이전에 진행되었던 방향을 알기 위해서 d 라는 변수를 추가한다
    global cnt
    if s > e:
        return

    mid = (s+e) // 2
    middle = nl[mid]
    if target == middle:
        cnt += 1
        return
    elif target < middle:   # left
        if direction == 1:
            return
        binarySearch(s, mid-1, target, 1)
    elif target > middle:   # right
        if direction == 2:
            return
        binarySearch(mid+1, e, target, 2)

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    nl = list(map(int, input().split())) # 길이가 A
    nl.sort()
    # quick(nl, 0, A-1)   # 이진탐색을 사용하기 위해서 퀵정렬을 이용하여 정렬한다.

    ml = list(map(int, input().split())) # 길이가 B
    cnt = 0
    for m in ml:
        binarySearch(0, A-1, m, 0)
    print(f"#{tc} {cnt}")
def merge_sort(m):
    if len(m) == 1:
        return

    left = right = []
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    # 왼쪽, 오른쪽 분할 정복
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
# 병합하는 함수
def merge(left, right):
    global cnt

    # 합병하기 전에 비교를 진행한다.
    if left[len(left)-1] > right[len(right)-1]:
        cnt += 1

    ln = len(left) # 0 <= li < ln
    rn = len(right)

    # left, right의 index를 각각 li, ri라고 한다.
    li = ri = 0
    result = []
    while li < ln or ri < rn:
        if li < ln and ri < rn:
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[li])
                ri += 1
        elif li < ln:
            result.append(left[li])
            li += 1
        elif ri < rn:
            result.append(right[ri])
            ri += 1
    return result




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

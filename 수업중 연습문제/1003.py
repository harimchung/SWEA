# quick sort 연습
def quicksort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right : # 찾을 데이터가 남은 상태

        # 왼쪽에는 피벗보다 작은 데이터만 남아야 한다 -> 피벗보다 크면 스탑
        while left <= end and array[left] <= array[pivot] :
            left += 1

        # 오른쪽에는 피벗보다 큰 데이터만 남아야 한다 -> 피벗보다 작으면 스탑
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 => right, pivot을 교체한다
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]

        # 엇갈린게 아니라면 => left, right을 교체한다
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 오른쪽을 기준으로 다시 정렬 수행한다.
    quicksort(array, start, right-1)
    quicksort(array, right+1, end)


a = [ 3, 4, 7, 1, 2, 10, 5, 6, 9 ]
quicksort(a, 0, len(a)-1)
print(a)
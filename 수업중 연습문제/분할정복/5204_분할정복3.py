def mergeSort(arr):
    global cnt
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    mergeSort(left)
    mergeSort(right)

    i, j = 0, 0
    il = 0
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[il] = left[i]
            i += 1
            il += 1
        else:
            arr[il] = right[j]
            j += 1
            il += 1

    while i < len(left):
        arr[il] = left[i]
        i += 1
        il += 1

    while j < len(right):
        arr[il] = right[j]
        j += 1
        il += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_arr = list(map(int, input().split()))
    cnt = 0
    mergeSort(num_arr)
    print(f"#{tc} {num_arr[N//2]} {cnt} ")
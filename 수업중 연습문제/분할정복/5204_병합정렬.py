# split and merge
def merge_sort(list):
    global cnt
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

def merge(left, right):
    global cnt
    i, j = 0, 0
    result = []

    while len(left) > i and len(right) > j:
        # if left[-1] >= right[-1]:
        #     cnt += 1

        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    print(merge_sort(num_list))
    # print(f"#{tc} {cnt} {merge_sort(num_list)[N//2]}")
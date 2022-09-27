def mergeSort(list):
    global cnt
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[-1] >= right[-1]:
                cnt += 1
                result.append(left.pop())
            else:
                result.append(right.pop())

        if len(left) > 0:
            result.append(left.pop())

        if len(right) > 0:
            result.append(right.pop())
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    print(mergeSort(num_list))
    print(cnt)
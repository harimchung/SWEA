T = int(input())

def quicksort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quicksort(A, l, s-1)
        quicksort(A, s+1, r)

def partition(A, l, r):
    p = A[l]
    i, j = l, r # i는 왼쪽에서 j는 오른쪽에서부터 탐색 시작
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <=j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print(f"#{tc} {arr[N//2]}")
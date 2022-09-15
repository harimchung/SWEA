def enq(n):
    global last
    last += 1
    heap[last] = n

    # 만약 추가되는 원소가 부모 노드보다 더 커버린 경우 자리를 바꿔줘야 한다.
    c = last # 새로 추가된 노드(자식노드)
    p = c // 2 # 부모노드

    # 부모가 존재하고, 부모 < 자식이면 자리 바꾸기,
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 혹시 바꾸고 난 다음에 또 바꿔야 할 수도 있기때문에 부모와 자식을 바꾼다.
        c = p
        p = c // 2
def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last = -1

    p = 1
    c = p*2

    # 자식이 있는 경우 비교 시작
    while c <= last:
        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면 비교대상을 오른쪽으로 한다.
        if c + 1<= last and heap[c] < heap[c+1]:
            c += 1

        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            # 혹시 바꾸고 난 다음에 또 바꿔야 할 수도 있기때문에 부모와 자식을 바꾼다.
            c = p
            p = c // 2
        else:
            break
    return tmp

heap = [0] * 100
last = 0
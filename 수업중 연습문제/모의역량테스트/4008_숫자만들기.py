def perm(i, k):
    global max_V, min_V
    if i == k:
        op_candidate.add(tuple(perm_operators))
        return

    else:
        for j in range(N-1):
            if not visited[j]:
                visited[j] = 1
                perm_operators[i] = operators[j]
                perm(i+1, k)
                visited[j] = 0

def add(list):
    tmp = numbers[0]
    for i in range(N-1):
        if list[i] == "+":
            tmp += numbers[i+1]
        elif list[i] == "-":
            tmp -= numbers[i+1]
        elif list[i] == "*":
            tmp *= numbers[i+1]
        else:
            tmp = int(tmp / numbers[i+1])
    return tmp

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_list = ["+", "-", "*", "/"]
    operator_number = list(map(int, input().split())) # 연산자의 개수는 N-1개이다.
    numbers = list(map(int, input().split())) # 연산자의 개수는 N-1개이다.

    min_V = 10**8
    max_V = -10**8


    operators = [] # 연산자의 개수를 가지고 만든 연산자 리스트
    i = 0 # 기본 리스트를 만드는 과정
    while i < 4:
        if operator_number[i] > 0:
            operators.append(op_list[i])
            operator_number[i] -= 1
        else:
            i += 1

    perm_operators = [0] * (N-1) # 연산자의 조합을 만들 리스트
    visited = [0] * (N-1) # 조합시에 사용할 방문 리스트
    # operators 를 가지고 permutation을 만든다.
    op_candidate = set()
    perm(0, N-1)
    print(op_candidate)
    # 각 조합에 대해서 연산을 진행한다.
    # 각 수식에 대해서 최댓값 / 최솟값을 갱신한다.
    # for candidate in (op_candidate):
    #     temp = add(candidate)
    #     if temp > max_V:
    #         max_V = temp
    #     if temp < min_V:
    #         min_V = temp

    print(f"#{tc} {max_V - min_V}")
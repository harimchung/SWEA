def p(i, k):# i는 레벨이자, weight의 인덱스. k는 내가 총 뽑아야 할 개수(여기에서는 tn)
    global max_V
    # 컨테이너의 수가 트럭수보다 작을 수 있기 때문에,
    # 모두다 골랐거나, 컨테이너가 부족할 경우에 weight를 비교해야 한다.

    if i == k:
        if sum(weight) > max_V:
            max_V = sum(weight)
        return

    else:
        for j in range(cn):
            if not visited[j]:
                visited[j] = 1
                if truck[i] >= cargo[j]:
                    weight[i] = cargo[j]
                p(i+1, k)
                visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    cn, tn = map(int, input().split())

    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 만약 화물의 수가 < 트럭의 수라면, 부족한 수만큼 0을 채워준다.
    if cn < tn:
        diff = tn - cn
        cargo.extend([0]*diff)
        cn = tn
    # 화물을 트럭의 개수만큼 뽑는 순열을 만든다.
    visited = [0]*cn    # visited는 cargo를 중복해서 뽑을 수 없기 때문에 만들었다.
    weight = [0]*tn     # weight는 총 truck에 담긴 무게를 구하기 위해 만들었다.
    max_V = 0
    p(0, tn)
    print(f"#{tc} {max_V}")

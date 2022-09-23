T = int(input())
for tc in range(1, T+1):
    cn, tn = map(int, input().split())

    cargo = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    visited = [0]*cn    # visited는 cargo를 중복해서 뽑을 수 없기 때문에 만들었다.
    weight = [0]*tn     # weight는 총 truck에 담긴 무게를 구하기 위해 만들었다.
    max_V = 0

    for i in range(tn):
        for j in range(cn):
            if truck[i] >= cargo[j] and not visited[j]:
                visited[j] = 1
                weight[i] = cargo[j]
                break
    print(f"#{tc} {sum(weight)}")


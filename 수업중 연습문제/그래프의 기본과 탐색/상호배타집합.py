
def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    return x

def find_set2(x): # 압축경로를 이용하면 부모테이블에 부모 노드 값이 갱신되어, 이후에 찾을 때 훨씬 빨라진다.
    if p[x] != x:
        p[x] = find_set2(p[x])
    return p[x]

def union(x,y):
    # x의 대표값으로 합하기
    p[find_set(y)] = find_set(x)

def union2(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if rank[y] > rank[x]:
        x, y = y, x

    # 랭크가 더 큰 집합에 속하도록 처리
    p[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1


V = 5 # V는 마지막 노드 번호의 수를 의미한다.
p = [i for i in range(V+1)] # make_set 즉, 자기자신이 대표가 되는 초기화 단계
rank = [0]*(V+1)

union2(1,2)
union2(1,3)
union2(2,4)

print(p)
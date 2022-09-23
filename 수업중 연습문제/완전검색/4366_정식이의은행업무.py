def bi_sum(len, num_list):
    temp = 0
    for j in range(len):
        temp += num_list[j]*(2**j)
    return temp

def tri_sum(len, num_list):
    temp = 0
    for j in range(len):
        temp += num_list[j]*(3**j)
    return temp

T = int(input())
for tc in range(1, T+1):
    bi_num = input()
    tr_num = input()
    bi = [int(num) for num in bi_num[::-1]]
    tr = [int(num) for num in tr_num[::-1]]

    possible_bi = []
    n = len(bi)
    for i in range(n):
        if bi[i] == 0:
            bi[i] = 1
            possible_bi.append(bi_sum(n, bi))
            bi[i] = 0
        else:
            bi[i] = 0
            possible_bi.append(bi_sum(n, bi))
            bi[i] = 1

    possible_tri = []
    m = len(tr)
    for k in range(m):
        if tr[k] == 0:
            tr[k] = 1
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 2
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 0
        elif tr[k] == 1:
            tr[k] = 0
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 2
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 1
        else:
            tr[k] = 0
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 1
            possible_tri.append(tri_sum(m, tr))
            tr[k] = 2

    for ans in possible_bi:
        if ans in possible_tri:
            break
    print(f"#{tc} {ans}")
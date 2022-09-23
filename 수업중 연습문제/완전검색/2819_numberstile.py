di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def path(i, j, cnt):
    while True:
        if cnt == 6:
            final_numbers.update(possible_numbers)
            return

        for _ in range(len(q)):
            ti, tj = q.pop(0)
            now = possible_numbers.pop(0)
            for d in range(4):
                ni, nj = ti+di[d], tj + dj[d]
                if 0 <= ni < 4 and 0 <= nj < 4:
                    possible_numbers.append(now+arr[ni][nj])
                    q.append((ni, nj))
        cnt += 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    final_numbers = set()
    for i in range(4):
        for j in range(4):
            si, sj = i, j
            possible_number = ""
            possible_number += arr[si][sj]
            possible_numbers = []
            q = []
            possible_numbers.append(possible_number)
            q.append((si,sj))
            path(si, sj, 0)
    print(f"#{tc} {len(final_numbers)}")
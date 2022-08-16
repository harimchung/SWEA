# ladder (사다리타기)

# 총 10개의 테스트 케이스가 주어지므로 아래 과정을 10번 반복한다.
for _ in range(10):
    # 첫 줄에는 테스트 케이스 번호가 주어진다.
    tc = int(input())

    # 100x100짜리 사다리 판이 주어진다.
    ladder = [list(map(int, input().split())) for __ in range(100)]

    # ladder의 마지막행에서 2인 값을 찾아
    # ladder을 거꾸로 타고 올라간다.

    # 현재 나의 위치 (ci, cj) = (99, for문에서 구한 j 값)
    ci = 99
    for j in range(100):
        if ladder[99][j] == 2:
            cj = j
            break

    # 어차피 마지막으로 내려오기 전은 확정이기 때문에 ci = 98부터 시작해도 된다.
    ci = 98
    # 현재 나의 위치가 첫 행 (즉 ci = 0이 될 때까지 반복한다)
    while ci > 0:
        # cj가 0~99 사이에 있고, 현재 기준 왼칸이 1이라면, 왼쪽으로 이동한다.
        if 0 < cj < 100 and ladder[ci][cj - 1] == 1:
            while ladder[ci][cj - 1] == 1:
                cj -= 1
                if cj == 0:
                    break
            ci -= 1
            # 만약 옆으로 이동한 칸도 값이 1이라면 계속이동한다.

        # cj가 0~99 사이에 있고, 현재 기준 오른쪽칸이 1이라면, 왼쪽으로 이동한다.
        elif 0 <= cj < 99 and ladder[ci][cj + 1] == 1:
            while (cj < 99) and ladder[ci][cj + 1] == 1:
                cj += 1
                if cj == 99:
                    break
            ci -= 1

        # 오른쪽, 왼쪽 다 1이아니라면, 위칸으로 이동한다.
        else:
            ci = ci - 1

    # ci = 0이 되었을 때, 즉 첫 행에 도착하면
    # 우리는 그 때의 j값을 찾아 출력하면 된다.
    print(f"#{tc} {cj}")
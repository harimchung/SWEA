T = int(input())
for tc in range (1, T+1):
    # N은 정수 (NxN짜리 배열을 만든다.)
    N = int(input())
    array = [[0]*N for _ in range(N)]

    # 움직일 수 있는 범위는 다음과 같다.(시계방향으로 채운다)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = 0

    ci, cj = 0, 0
    value = 1
    # 처음 시작점을 1로 채우고 시작한다.
    array[ci][cj] = value

    # value 값이 N*N이 될 때까지 채우기를 반복한다.
    while value < N*N:
        # 다음은 어디로 갈까? di를 따라서 이동해본다.
        # d의 범위는 0, 1, 2, 3이기 때문에 다음과 같은 식을 추가한다.
        # 4로 나눈 나머지는 0,1,2,3 중 하나기 때문에
        for i in range(4):
            d = (d+i)%4
            ni = ci + di[d]
            nj = cj + dj[d]

            # 만얀 ni, nj가 범위 안에 있고 값이 영이라면 방향찾기를 종료한다.
            if 0<= ni <N and 0<= nj <N and array[ni][nj]==0:
                ci = ni
                cj = nj
                break;

        # 값 채우기
        value += 1
        array[ci][cj] = value

    # 출력하기
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(array[i][j], end=" ") #숫자 사이에 빈칸
        print() # 한줄씩 개행해서 예쁘게
t = int(input())

# 테스트케이스에대해서 t번 반복한다.
for tc in range(1, t+1):
    n, k = map(int, input().split())

    # 퍼즐을 이차원배열로 입력받는다.
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # 퍼즐에서는 0은 이미 채워진 칸이고, 1은 빈칸이다
    # 연속된 빈칸의 개수가 k와 같으면 ans에 1을 추가한다.
    # 그렇다면 어떻게 연속된 1을 찾느냐?
    ans = 0

    # 1. 행에서 연속된 1찾기
    # 각 행에 대해서 1이 나오면 cnt를 1추가,
    # 0이 나오면 우선 기존의 cnt 값이 k값과 같은지 비교한 후,
    # 다시 cnt를 0으로 초기화 한다.


    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            else :
                if cnt == k:
                    ans += 1
                cnt = 0

        # 위 코드에서 끝나면, 1로 끝난 경우 ans에 추가가 안되기 때문에
        # 한 줄 더 추가
        if cnt == k:
            ans += 1


    # 2. 열에서 연속된 1찾기
    # 방법은 동일하다.
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            else :
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1


    print(f"#{tc} {ans}")
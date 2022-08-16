# 테스트 케이스의 수를 입력받는다.
T = int(input())
# 테스트케이스의 넘버는 1~T 까지
for tc in range(1, T+1):
    # 테스트 케이스를 한번 순회할 때마다, 0으로 찬 10x10짜리 테이블을 만든다.
    list1 = [[0]*10 for _ in range (10)]
    list2 = [[0]*10 for _ in range (10)]

    # 칠할 영역의 개수가 주어진다.
    # 즉 n 번 동안 이 작업을 반복한다.
    n = int(input())
    for __ in range(n):
        # 처음 모서리와 끝모서리, 색깔 정보를 담은 정보를 color_info 라는 어레이에 할당한다.
        color_info = list(map(int, input().split()))
        # color_info 리스트의 각 인덱스별로 시작 x,y 좌표 끝 x, y좌표를 의미하는 변수에 할당한다.
        start_i = color_info[0]
        start_j = color_info[1]
        end_i = color_info[2]
        end_j = color_info[3]

        # color_info의 마지막 수는 1혹은 2이고
        # 마지막 수가 1이라면 list 1에, 아니라면 list2에 추가한다.
        if color_info[-1] == 1:
            for i in range (start_i, end_i+1):
                for j in range (start_j, end_j+1):
                    list1[i][j] = 1

        else:
            for i in range(start_i, end_i + 1):
                for j in range(start_j, end_j + 1):
                    list2[i][j] = 1

    cnt = 0
    for i in range(10):
        for j in range(10):
            if list1[i][j] == 1 & list2[i][j] == 1:
                cnt += 1

    print(f"#{tc} {cnt}")
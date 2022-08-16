T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    number_list = [0]*10
    # 일단 스도쿠가 될 수 있는 변수를
    is_sudoku = 1

    # 1.가로 줄에대해서 스도쿠인지 판별
    # i는 각각 가로줄의 인덱스를 의미한다.
    for i in range(9):
        # 각 가로줄의 숫자에 대해서
        for number in sudoku[i]:
            # 숫자가 나오면, 숫자리스트에있는 '0'을 '1'로 바꾼다.
            number_list[number] = 1

        for j in range (1, 10):
            if number_list[j] != 1:
                is_sudoku = 0

    # 2. 세로 줄에 대해서 스도쿠인지 판별

    # 3. 3x3칸에 대해서 스도쿠인지 판별


    print(f"#{tc} {is_sudoku}")
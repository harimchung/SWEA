# 10번 반복한다.
for _ in range(10):
    tc = int(input())
<<<<<<< HEAD
    array = [list(map(int, input().split())) for _ in range(100)]
=======
    array = [list(map(int, input().split())) for _ in range(10)]
>>>>>>> 203583e715f588f7fd0e1bf0530913fad53169d5

    # 나중에 최대값을 출력할 max라는 변수를 하나 만든다.
    # 1회 반복 후 다시 0으로 초기화 시킨다.
    max = 0

    # 1. 행의 합
    for i in range(100):
        # 행 한 줄 끝날때마다 sum의 값은 0으로 초기화 시킨다.
        sum = 0
<<<<<<< HEAD
        for j in range(100):
=======
        for j in r
            
            ange(100):
>>>>>>> 203583e715f588f7fd0e1bf0530913fad53169d5
            # sum이라는 변수에 각 행에 해당하는 요소를 추가시킨다.
            sum += array[i][j]
            # 만약 최대값이 max 보다 크면, max를 바꾼다.
            if sum > max:
                max = sum

    # 2. 열의 합
    for i in range(100):
        # 열 한 줄 끝날때마다 sum의 값은 0으로 초기화 시킨다.
        sum = 0
        for j in range(100):
            # sum이라는 변수에 각 행에 해당하는 요소를 추가시킨다.
            sum += array[j][i]
            # 만약 최대값이 max 보다 크면, max를 바꾼다.
            if sum > max:
                max = sum

    # 3. 대각선의 합
    for i in range(100):
        # 대각선 한 줄이 끝날 때마다 sum은 초기화시킨다.
        sum = 0
        sum += array[i][i]
        # 만약 최대값이 max 보다 크면, max를 바꾼다.
        if sum > max:
            max = sum

    # 4. 반대 대각선의 합
    for i in range(100):
        # 대각선 한 줄이 끝날 때마다 sum은 초기화시킨다.
        sum = 0
<<<<<<< HEAD
        sum += array[99 - i][i]
        # 만약 최대값이 max 보다 크면, max를 바꾼다.
        if sum > max:
            max = sum
    print(f"#{tc} {max}")
=======
        sum += array[99-i][i]
        # 만약 최대값이 max 보다 크면, max를 바꾼다.
        if sum > max:
            max = sum
    print(f"#{tc} max")
>>>>>>> 203583e715f588f7fd0e1bf0530913fad53169d5

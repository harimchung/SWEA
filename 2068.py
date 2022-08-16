# T는 입력받은 테스트케이스의 개수이다.
T = int(input())

# 입력받은 테스트케이스만큼 반복한다. 단, 1부터 시작하기 위해서 range값을 조정한다.
for t in range (1, T+1):
    ai=list(map(int, input().split()))
    for index in range (0, 9):
        if ai[index] > ai[index+1]:
            ai[index] , ai[index + 1] = ai[index+1] , ai[index]
    print(f"#{t} {ai[-1]}")


# T는 주어진 테스트 케이스의 수
T = int(input())

# 테스트 케이스의 수 만큼 아래를 반복한다.
# 나중에 테스트케이스 앞에 쓰는 숫자를 1부터 쓰기 위해서, range를 1부터로 시작했다.
for _ in range (1, T+1):
    # N은 카드 장수, ai는 여백없이 주어진 카드 숫자이다.
    N = int(input())
    ai = list(int(i) for i in input())

    # 각각의 숫자가 몇 번 나왔는지 기록할 bi 리스트를 만든다
    bi = [0]*10
    for a in ai:
        bi[a] += 1

    # 가장 많이 나온 숫자를 찾기 위해서, 인덱스를 활용해서
    # bi 값이 가장 큰 인덱스를 찾는다.
    # 같은 횟수로 나왔을 경우, 큰 수를 뽑아야 하기 때문에 뒤에서부터 뒤진다.
    max_index = 9
    for index in range(8, -1, -1):
        if bi[max_index] < bi[index]:
            max_index = index

    print(f"#{_} {max_index} {bi[max_index]}")
T = int(input())
def solve(opers, exp, idx):
    global minV, maxV
    if idx == N-1:
        # 재귀함수를 끝내는 조건
        exp = list(exp)

        # 연산자와 숫자를 통해서 식을 계산한다.
        ni = 0
        result = nums[ni]

        # 연산자 하나씩 꺼내고, 숫자도 하나씩 꺼내서 결과 계산
        while exp:

            ni += 1
            right = nums[ni]
            op = exp.pop(0)

            if op == "+":
                result += right
            elif op == "-":
                result -= right
            elif op == "*":
                result *= right
            else:
                result = int(result / right)

        if minV > result:
            minV = result
        if maxV < result:
            maxV = result

        return
    # 현재 자리에 넣을 수 있는 연산자 넣기
    # 남은 개수가 0개 이상이면 넣을 수 있다.
    if opers[0] > 0:
        opers[0] -= 1
        solve(opers, exp+"+", idx+1)
        opers[0] += 1

    if opers[1] > 0:
        opers[1] -= 1
        solve(opers, exp+"-", idx+1)
        opers[1] += 1

    if opers[2] > 0:
        opers[2] -= 1
        solve(opers, exp+"*", idx+1)
        opers[2] += 1

    if opers[3] > 0:
        opers[3] -= 1
        solve(opers, exp+"/", idx+1)
        opers[3] += 1


for tc in range(1, T+1):
    N = int(input())
    operations = list(map(int, input().split()))
    # operations => 사용 가능 횟수를 담은 리스트
    nums = list(map(int, input().split()))

    maxV = -100000000
    minV = 100000000
    solve(operations, "", 0)
    print(f"#{tc} {maxV - minV}")
def get_prime(a, b):
    arr = [True] * (b + 1)  # 일단 n까지의 숫자를 다 소수라고 표시

    m = int((b) ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:  # 만약 i 번째 수가 소수라면,
            # 소수의 배수를 모두 소수가 아니라고 체크한다.
            for j in range(i + i, b + 1, i):
                arr[j] = False
    return [i for i in range(a, b + 1) if arr[i] == True]

T = int(input())
for tc in range(1, T+1):
    d, a, b = map(int, input().split())


    print(f"#{tc} {get_prime(a, b)}")
# n은 총 주어진 테스트케이스의 수 이다
n = int(input())
for test_case_number in range(1, n + 1):
    i = int(input())
    numbers = list(map(int, input().split()))
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    for number in numbers:
        if number < min_number:
            min_number = number

    print(f"#{test_case_number} {max_number-min_number}")

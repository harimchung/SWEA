# 회문 검사의 가장 기본
# 뒤집어서 같은 수이면 == 회문이다

def is_palindrome(list, n, m):
    # 1. 행 우선 순회
    # 각각의 행에 대해서 순회한다.
    for i in range(n):
        # 빈 문자열을 만들어 더해보자
        # j의 범위는 만약 n, m 이 같지 않다면, [0,1,2,3,4,5,6,7,8,9] 에서 n=10, m =6이다. 이때 m의 시작 인덱스는 4, 즉 n-m 까지 갈 수 있으므로 끝 범위는 n-m+1로 지정한다.
        for j in range (0, n-m+1):
            word_row = ""
            for k in range(m):
                word_row += list[i][j+k]

        # 순회가 끝난 후 만약 word_row의 값이 회문이라면 회문을 출력한다.
            if word_row == word_row[::-1]:
                return word_row

    # 2. 열 우선 순회
    for i in range(n):
        # 빈 문자열을 만들어 더해보자
        # j의 범위는 만약 n, m 이 같지 않다면, [0,1,2,3,4,5,6,7,8,9] 에서 n=10, m =6이다. 이때 m의 시작 인덱스는 4, 즉 n-m 까지 갈 수 있으므로 끝 범위는 n-m+1로 지정한다.
        for j in range(0, n - m + 1):
            word_column = ""
            for k in range(m):
                word_column += list[j + k][i]

            # 순회가 끝난 후 만약 word_row의 값이 회문이라면 회문을 출력한다.
            if word_column == word_column[::-1]:
                return word_column

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # n개의 글자를 가진 n개의 줄이 주어진다. (정사각형 배열)
    # 2차원 배열의 list 형태로 받는다.
    words = [list(input()) for _ in range(n)]

    # 회문검사
    print(f"#{tc}", end=" ")
    print(is_palindrome(words, n, m))
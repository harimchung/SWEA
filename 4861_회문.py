def is_palindrome(list, n, m):
    # 리스트와 숫자(n)이 주어지면 회문인지 검사하는 함수를 생성한다.
    # [A,B,C,B,A]
    # n = 5, m = 2
    mid = m // 2
    # 1. 가로줄에 대한 검사 (행 우선순회)


    for i in range(n): # 각 한 줄 별로 검사한다.
        for j in range(n-m+1):
            # 각 줄별로 새로운 미니 list를 만든다.
            mini_list = list[i][j:j+m+1]
            cnt = 0
            for k in range(mid):
                if mini_list[k] == mini_list[-(k + 1)]:
                  cnt += 1
                if cnt == mid:
                    return "".join(mini_list)

    for i in range(n): # 각 행 별로 검사한다.
        for j in range(n-m+1):
            # 각 줄별로 새로운 미니 list를 만든다.
            word_column = ""
            for k in range(m):
                word_column += list[j+k][i]

            if word_column == word_column[::-1]:
                return word_column
T = int(input())
for tc in range (1, T+1):
    n, m = map(int, input().split())

    # n개의 글자를 가진 n개의 줄이 주어진다. (정사각형 배열)
    # 2차원 배열의 list 형태로 받는다.
    words = [list(input()) for _ in range(n)]

    # 회문검사
    print(f"#{tc}", end=" ")
    print(is_palindrome(words,n,m))


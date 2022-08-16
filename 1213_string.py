for _ in range (10):
    tc = int(input())
    # 찾아야 하는 단어는 p로 주어진다.
    p = input()
    n = len(p) # 문자열의 길이는 n

    # 주어진 문자열은 s로 주어진다.
    s = input()
    m = len(s)

    cnt = 0
    # 고지식한 패턴찾기를 통해 반복한다.
    i = 0 # 문자열의 인덱스는 i
    j = 0 # 찾아야 하는 단어의 인덱스는 j

    while j < n and i < m:
        if s[i] != p[j] :
            i = i - j
            j = -1


        elif s[i] == p[j]:

            if j == n - 1 :
                cnt += 1
                j = -1

        i = i + 1
        j = j + 1

    print(f"#{tc} {cnt}")
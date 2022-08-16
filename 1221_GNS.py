# GNS
# 처음에는 테스트케이스의 번호가 주어진다.
T = int(input())

for tc in range(1,T+1):
    # #1 7041 의 형태로 번호와 문자열의 길이를 입력받는다.
    number, n = input().split()
    n = int(n)
    # 정렬되기 전 문자열을 s로 입력받는다.
    s = input()
    k = len(s)
    # 각 숫자의 개수룰 셀 카운트 리스트를 하나 만든다.
    count = [0]*10
    num_str = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]

    # 문자열에서 3칸씩 건너뛰면서 어떤 숫자가 나왔는지 숫자를 센다
    # 각 숫자를 구별하려면, 첫 두 문자만 비교하면 된다.
    # 각 문자가 몇번 씩 나왔는지 개수를 세서 카운트에 회수를 구한다.
    for i in range (0, k, 4):
       if s[i]=="Z" and s[i+1]=="R":
           count[0] += 1
       if s[i] == "O" and s[i + 1] == "N":
           count[1] += 1
       if s[i] == "T" and s[i + 1] == "W":
           count[2] += 1
       if s[i] == "T" and s[i + 1] == "H":
           count[3] += 1
       if s[i] == "F" and s[i + 1] == "O":
           count[4] += 1
       if s[i] == "F" and s[i + 1] == "I":
           count[5] += 1
       if s[i] == "S" and s[i + 1] == "I":
           count[6] += 1
       if s[i] =="S" and s[i+1]=="V":
           count[7] += 1
       if s[i] == "E" and s[i + 1] == "G":
           count[8] += 1
       if s[i] == "N" and s[i + 1] == "I":
           count[9] += 1


    print(f"{number}")
    for i in range(10):
        if count[i] != 0:
            print(num_str[i]*count[i], end="")
    print()
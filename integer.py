# 에라토스테네스의 체를 이용해서 소수인지 아닌지 판별하기
def is_primnumber(n):
    # 일단 모든 값이 소수라고 (True)라고 표시
    table = [True]*(n+1)
    # table의 i 번째 값이 True라면
    for i in range(2, n):
        if table[i]:
            for j in range (i+i, n+1, i):
                table[j] = False
    return [i for i in range(2, n+1) if table[i]==True]

print(is_primnumber(100)) #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime_number2(n):
    table = [True]*(n+1)
    m = int(n**0.5)
    for i in range (2,m+1):
        if table[i]:
            for j in range(i+i, n+1, i):
                table[j] = False
    return [i for i in range(2,n+1) if table[i]==True]

print(is_prime_number2(100))
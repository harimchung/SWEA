def my_swap(a):
    n = len(a)
    string_list = list(a)
    for i in range(n//2):
        string_list[i],string_list[n-1-i] = string_list[n-1-i],string_list[i]
    return "".join(string_list)

def my_swap_2(a):
    n = len(a)
    new_string = ""
    for i in range (n-1,-1,-1):
        new_string += a[i]
    return new_string

print(my_swap("Hello World!"))
print(my_swap_2("Hello World!"))

def my_strcmp(str1, str2):
    if str1 < str2:
        return -1 # str1 이 사전순으로 앞서면 (아스키코드 값이 더 작으면) -1을 출력
    elif str1 > str2:
        return 1
    else :
        return 0

print(my_strcmp('apple', 'banana'))
print(my_strcmp('apple', 'appe'))
print(my_strcmp('banana', 'balloons'))

def s_to_i(string1):
    # 입력받은 문자열을 아스키코드 (ord)를 이용해서 숫자로 변환한다
    # 예를 들어 '123' 이 들어온 경우, 문자열은 순회 가능하므로
    # 1, 2, 3이 차례로 들어온다.
    # ord의 차를 이용하면, 숫자를 구할 수 있다.
    i = 0
    for x in string1:
        i = i*10 + ord(x) - ord('0')
    return i

print(s_to_i('123'))

def i_to_s(integer):
    # 입력받은 정수를 아스키코드(chr)을 이용해서 문자열로 변환한다.
    # 예를 들어 123이란 정수가 들어온 경우, 10으로 나누고 나머지를 더하는 과정을 통해서
    # 빈 문자열에 더한다. 그러면 321 이 나오게 되므로
    # 역으로 뒤집는 과정을 마지막에 넣는다.
    i = ""
    while integer > 0:
        i += chr(ord('0') + integer%10)
        integer = integer//10
    return i[::-1]

print(i_to_s(123))
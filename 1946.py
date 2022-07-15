test_num = int(input())
x = 1
for y in range(test_num):

    case_num = int(input())

    case = [input().split() for i in range(case_num)]

    empty = []

    for j in range(case_num):
        result = str(case[j][0]*int(case[j][1]))
        empty.append(result)
        result_string = ('').join(j for j in empty)

    print(f'#{x}')
    for k in range (0, len(result_string), 10):
        print(result_string[k:k+10])

    x += 1



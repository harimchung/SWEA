import sys
stack = []
# push
def push(n):
    return stack.append(n)
#pop
def pop():
    # 만약 stack의 원소가 존재한다면
    if stack:
        # 가장 위에 있는 정수를 출력한다
        a = stack[-1]
        print(a)
        # 그리고 그 수를 제거한다.
        stack.pop(-1)
    else :
        print(-1)
# size
def size():
    print(len(stack))

def empty():
    if stack :
        print("0")
    else :
        print("1")

def top():
    if stack:
        print(stack[-1])
    else:
        print("-1")

T = int(input())
for _ in range(T):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        n = order[1]
        push(n)
    if order[0] == "pop":
        pop()
    if order[0] == "size":
        size()
    if order[0] == "empty":
        empty()
    if order[0] == "top":
        top()

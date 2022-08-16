a = [2,3,5]
n = len(a)

for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            print(a[j], end=" ")
    print()
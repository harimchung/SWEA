a = int(input())
b = a % 10
c = (a%100)
f = int((c-b)/10)
d = (a%1000)-c
g = int(d/100)
e = a // 1000
i = b + f + g + e
print(i)
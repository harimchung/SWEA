n = int(input())
data = [input() for i in range(n)]
j = 1
for word in data:
    if list(word) == list(reversed(word)):
        print(f"#{j} 1")
      
    else : 
        print(f"#{j} 0")
    j+=1
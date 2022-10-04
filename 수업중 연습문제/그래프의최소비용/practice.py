# a = [(1,2,3), (2,3,4)]
# s,e,w = a.pop(0)
# print(s)
# print(e)
#
# V, E = map(int, input().split())
#
#
# adj = []
# for _ in range(E):
#     n1, n2, w = map(int, input().split())
#     adj.append((n1, n2, w))
#
# adj.sort(key=lambda x:x[2])
# weight = 0
# cnt = 0
#
# p = [ i for i in range (V+1)]
#
# while True:
#     # 모든 정점에 방문했다면, 방문을 종료한다.
#     if cnt == V: # 최소 간선의 개수만큼 골랐다면 종료한다.
#         break
#
#     s, e, w = adj.pop(0)
#     # 시작점과 종료지점에 대해서 대표가 같다면, continue
#     if find_set(s) == find_set(e):
#         continue
#     else:
#         cnt += 1
#         union(s,e)
#         weight += w

import heapq

q = [] # 기본적으로 heapq는 최소힙이기 때문에 제일 적은값이 앞에 저장되는 구나.
heapq.heappush(q, 2)
print(q)
heapq.heappush(q, 1)
print(q)
heapq.heappush(q, 5)
print(q)
heapq.heappush(q, 3)
print(q)
heapq.heappush(q, 8)
print(q)
heapq.heappop(q)
print(q)
heapq.heappop(q)
print(q)
heapq.heappop(q)
print(q)

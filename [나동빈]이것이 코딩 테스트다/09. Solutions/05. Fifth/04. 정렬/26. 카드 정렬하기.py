from sys import stdin
import heapq

q = []
result = 0
for _ in range(int(stdin.readline())):
    heapq.heappush(q, int(stdin.readline()))

while len(q) > 1:
    a, b = heapq.heappop(q), heapq.heappop(q)
    result += (a + b)
    heapq.heappush(q, (a + b))

print(result)
from sys import stdin
import heapq

cards = []

for _ in range(int(stdin.readline())):
    heapq.heappush(cards, int(stdin.readline()))


result = 0

while len(cards) > 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    result += a + b
    heapq.heappush(cards, a + b)

print(result)
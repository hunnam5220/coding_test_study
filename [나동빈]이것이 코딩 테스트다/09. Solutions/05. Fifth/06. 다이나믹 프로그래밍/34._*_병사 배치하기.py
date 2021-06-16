from sys import stdin

n = int(stdin.readline().split())
s = list(map(int, stdin.readline().split()))
s.sort(reverse=True)

cnt = 1

for i in range(n):

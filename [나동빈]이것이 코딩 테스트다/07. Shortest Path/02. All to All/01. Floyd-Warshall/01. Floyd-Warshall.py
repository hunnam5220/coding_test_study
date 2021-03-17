from sys import stdin

""" 무한을 뜻하는 INF 변수에 10억을 저장 """
INF = int(1e9)

""" 노드의 개수 및 간선의 개수 입력 받기 """
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

""" n * n (노드 개수 제곱)만큼 빙고판 만들기 """
graph = [[INF] * n for _ in range(n)]

""" 출발 노드와 도착 노드가 같으면 0을 입력 """
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print("I", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
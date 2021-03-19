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

""" 간선에 대한 정보를 입력받기 """
for _ in range(m):
    """ A 노드에서 B 노드로 가는 비용을 C라고 한다. """
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = c

""" 점화식에 따라 플로이드 워셜 알고리즘 수행 """
for k in range(n):
    for a in range(n):
        for b in range(n):
            """ 
            A 노드에서 B 노드로 가는 비용과
            A 노드에서 K 노드 + K 노드에서 B 노드로 가는 비용을 비교 
            """
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

""" 출력 """
for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print("%3s" % 'I', end='')
        else:
            print("%3d" % graph[a][b], end=' ')
    print()
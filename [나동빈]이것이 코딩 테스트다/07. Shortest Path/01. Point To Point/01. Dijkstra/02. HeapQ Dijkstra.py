import heapq
from sys import stdin

""" 무한을 뜻하는 INF 변수에 10억을 저장 """
INF = int(1e9)

""" 노드의 개수, 간선의 개수를 입력 받음 """
n, m = map(int, stdin.readline().split())

""" 출발 노드를 입력 받음 """
start_node = int(stdin.readline().rstrip())

""" 각 노드가 연결되어 있는 정보를 담을 리스트를 생성 """
graph = [[] for _ in range(n)]

""" 거리값을 비교하고 갱신해줄 리스트를 생성 """
distance = [INF] * n

""" 각 노드가 연결되어 있는 정보를 입력받은 간선의 개수만큼 입력 받음 """
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    """ a번 노드에서 b노드로 가는데 c만큼의 비용이 든다 이 새끼야 씨발아 알겠냐? """
    graph[a - 1].append([b - 1, c])
 

def dijkstra(start_node):
    """ 힙큐로 사용할 리스트 생성 """
    q = []

    """ 힙큐에 거리, 현재 노드 정보를 넣어 줌 """
    heapq.heappush(q, (0, start_node - 1))

    """ distance 리스트, 0번째 배열에 거리를 입력 """
    distance[start_node - 1] = 0

    """ 힙큐가 비어질 때까지 반복 """
    while q:
        """ 거리 및 현재 노드정보를 힙큐에서 빼옴 """
        dist, now = heapq.heappop(q)

        """ 만약 현재 노드에 해당의 거리값이 distance 배열에 있는 거리값보다 크면 무시 """
        if distance[now] < dist:
            continue

        """ 만약 현재 노드에 해당의 거리값이 distance 배열에 있는 거리값보다 작으면 """
        """ 현재 노드에 연결되어 있는 노드들이 있는 리스트를 반복문으로 꺼내서 """
        for i in graph[now]:

            """ i[0] 번 노드까지 가는데 i[1] 만큼의 비용이 든다 """
            """ cost 변수에 현재 노드를 거쳐 다른 노드로 이동하는 비용을 저장 """
            cost = dist + i[1]

            """ cost가 distance 리스트의 i[0]번 노드에 저장되어 있는 값보다 작으면 """
            if cost < distance[i[0]]:

                """ distance 리스트의 i[0]번 노드에 저장되어 있는 값을 cost(최단거리 값)으로 갱신해준다. """
                distance[i[0]] = cost

                """ 힙큐에 갱신한 값(거리) 와 노드 정보를 넣어준다. """
                heapq.heappush(q, (cost, i[0]))


""" 힙큐 최단거리 알고리즘 시작! """
dijkstra(start_node)

""" distance 배열을 하나씩 뽑아서 """
for i in distance:

    """ 거리값이 무한이면 INFINITY 출력 """
    if i == INF:
        print('INFINITY')
    else:
        """ 아니면 최단거리 값 출력 """
        print(i)
"""
* 넓이 우선 탐색 (Breadth First Search)
* * Workflow * *
 - 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
 - 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 후 방문처리
 - 3. 2~3 과정을 반복할 수 없을 때까지 반복.
"""
from collections import deque as dq


def bfs(graph, root_node, visited):
    pass


graph = [
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * len(graph)
root_node = 1
bfs(graph, root_node, visited)

# answer : 1 2 3 8 7 4 5 6

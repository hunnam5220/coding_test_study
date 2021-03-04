"""
* 깊이 우선 탐색 (Depth First Search)
* * Workflow * *
 - 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
 - 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
 - 3. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
 - 4. 2~3 과정을 반복할 수 없을 때까지 반복.
"""


def dfs(graph, root_node, visited):
    visited[root_node - 1] = True
    print(root_node, end=' ')

    for step in graph[root_node - 1]:
        if not visited[step - 1]:
            dfs(graph, step, visited)


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
root_node = 1
visited = [False] * len(graph)
print('result : ', end='')
dfs(graph, root_node, visited)

# answer : 1 2 7 6 8 3 4 5
print('\nanswer : 1 2 7 6 8 3 4 5')
from collections import deque as qq


def bfs(graph, root_node):
    visited = [root_node]

    for x in range(root_node, len(graph)):
        queue = qq(graph[x])
        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)

            for y in graph[n]:
                if y not in visited:
                    queue.append(y)
                    
    return visited


graph = [
    [],
    [2, 7, 3],
    [1, 4, 5],
    [1, 6],
    [2, 10],
    [2],
    [3, 9, 11],
    [1, 8, 9],
    [7], [7],
    [4, 12, 13],
    [6],
    [10, 14, 15],
    [10],
    [12],
    [12]
]
root_node = 1

print(bfs(graph, root_node))
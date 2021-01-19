def dfs(graph, root_node):
    visited = []
    stack = [root_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            graph[node].reverse()
            stack.extend(graph[node])

    return visited


graph = [
    [],
    [2, 7, 3],
    [1, 4, 5],
    [1, 6],
    [2, 10], [2],
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
print(dfs(graph, root_node))
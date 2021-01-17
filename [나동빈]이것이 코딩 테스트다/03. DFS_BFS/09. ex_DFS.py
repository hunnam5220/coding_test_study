def dfs(graph, stack, visited, step):
    while False not in visited:
        stack.append(step)
        visited[step-1] = True





graph = [
    [],
    [2, 3, 7],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3, 9],
    [1, 8, 9],
    [7],
    [6, 7]
]
visited = [False] * len(graph)
step = 1
stack = []

dfs(graph=graph, stack=stack, visited=visited, step=step)
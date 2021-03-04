from sys import stdin


def dfs(arr, root_node, visited):
    pass


n, m = map(int, stdin.readline().rstrip().split())
arr = []

for step in range(n):
    arr.append(list(stdin.readline().rstrip()))

root_node = 1
visited = [False] * (n * m)
dfs(arr, root_node, visited)
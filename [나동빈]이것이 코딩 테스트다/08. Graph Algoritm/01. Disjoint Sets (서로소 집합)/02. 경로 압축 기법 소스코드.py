def find_parent(parent, x):
    if parent[x - 1] != x:
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]
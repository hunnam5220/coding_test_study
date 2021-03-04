"""
* Adjacency Matrix (인접 행렬) 방식
* 인접 행렬 방식은 2차원 배열에 각 노드가 연결되어 있는 형태를 나타낸 것.
"""

INF = 99999999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
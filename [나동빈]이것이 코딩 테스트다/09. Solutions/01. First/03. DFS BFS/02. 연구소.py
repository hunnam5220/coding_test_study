from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []

for step in range(n):
    graph.append(list(map(int, stdin.readline().split())))

result = [0]

def infection(x, y):
    """ 바이러스 퍼지게 하기 """

    pass


def install(count):
    """ 울타리 설치하기 """
    if count == 3:

        result[0] = max(result[0], get_area_zero())
        return
    for x in range(n):
        for y in range(m):
            

def get_area_zero():
    return
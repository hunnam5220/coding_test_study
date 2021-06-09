from bisect import *


def get_res(arr, s, e):
    return bisect_right(arr, e) - bisect_left(arr, s)


def solution(words, queries):
    answer = []

    nw = [[] for _ in range(10001)]
    rw = [[] for _ in range(10001)]

    for word in words:
        n = len(word)
        nw[n].append(word)
        rw[n].append(word[::-1])

    for i in range(10001):
        nw[i].sort()
        rw[i].sort()

    for q in queries:
        n = len(q)
        if q[0] != '?':
            res = get_res(nw[n], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = get_res(rw[n], q.replace("?", "a")[::-1], q.replace("?", "z")[::-1])

        answer.append(res)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

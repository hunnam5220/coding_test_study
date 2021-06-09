from bisect import bisect_left, bisect_right


def get_idx(arr, start, end):
    return bisect_right(arr, end) - bisect_left(arr, start)


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
            res = get_idx(nw[n], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = get_idx(rw[n], q.replace("?", "a")[::-1], q.replace("?", "z")[::-1])

        answer.append(res)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
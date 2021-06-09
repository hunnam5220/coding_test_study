from bisect import bisect_left, bisect_right


def get_idx(arr, start, end):
    return bisect_right(arr, end) - bisect_left(arr, start)


n_w = [[] for _ in range(10001)]
r_w = [[] for _ in range(10001)]
r = []


def solution(words, queries):
    for word in words:
        n = len(word)
        n_w[n].append(word)
        r_w[n].append(word[::-1])

    for i in range(10001):
        n_w[i].sort()
        r_w[i].sort()

    for q in queries:
        n = len(q)
        if q[0] != "?":
            res = get_idx(n_w[n], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = get_idx(r_w[n], q.replace("?", "a")[::-1], q.replace("?", "z")[::-1])
        r.append(res)

    return r


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
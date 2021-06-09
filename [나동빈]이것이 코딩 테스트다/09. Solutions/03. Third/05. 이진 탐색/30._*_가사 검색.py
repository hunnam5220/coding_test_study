from bisect import bisect_left, bisect_right


def get_index(arr, start, end):
    a = bisect_right(arr, end)
    b = bisect_left(arr, start)
    return a - b


n_word = [[] for _ in range(10001)]
r_word = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    for word in words:
        n = len(word)
        n_word[n].append(word)
        r_word[n].append(word[::-1])

    for i in range(10001):
        n_word[i].sort()
        r_word[i].sort()

    for q in queries:
        if q[0] != '?':
            h = get_index(n_word[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else:
            h = get_index(r_word[len(q)], q.replace("?", "a")[::-1], q.replace("?", "z")[::-1])
        answer.append(h)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

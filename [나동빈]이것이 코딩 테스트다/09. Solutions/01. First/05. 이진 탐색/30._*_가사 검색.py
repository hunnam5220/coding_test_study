from bisect import bisect_left, bisect_right


def get_words(arr, left_val, right_val):
    return bisect_right(arr, right_val) - bisect_left(arr, left_val)


def solution(words, queries):
    answer = []
    nor_w = [[] for _ in range(10001)]
    rev_w = [item[:] for item in nor_w]

    for step in words:
        nor_w[len(step)].append(step)
        rev_w[len(step)].append(step[::-1])

    for step in range(10001):
        nor_w[step].sort()
        rev_w[step].sort()

    for q in queries:
        if q[0] != '?':
            result = get_words(nor_w[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            result = get_words(rev_w[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(result)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
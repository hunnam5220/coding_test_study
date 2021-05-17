import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    f_len = len(food_times)
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i + 1])

    pre, sv = 0, 0

    while sv + ((q[0][0] - pre) * f_len) < k:
        ft, fnum = heapq.heappop(q)

        sv += (ft - pre) * f_len
        f_len -= 1
        pre = ft

    q.sort(key=lambda x: x[1])

    return q[(k - sv) % f_len][1]


# 1
print(solution([3, 1, 2], 5))

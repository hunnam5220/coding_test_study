import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    length = len(food_times)
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i + 1])

    pre, sv = 0, 0

    while sv + ((q[0][0] - pre) * length) < k:
        f_time, f_num = heapq.heappop(q)
        sv += (f_time - pre) * length

        length -= 1
        pre = f_time

    q.sort(key=lambda x: x[1])

    return q[(k - sv) % length][1]


# 1
print(solution([3, 1, 2], 5))

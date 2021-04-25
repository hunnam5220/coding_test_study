import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    new_foodtimes = []
    leng = len(food_times)
    for x in range(1, leng + 1):
        heapq.heappush(new_foodtimes, [food_times[x - 1], x])

    pre, eat_time, now = 0, 0, 0
    while eat_time + ((new_foodtimes[0][0] - pre) * leng) < k:
        now, idx = heapq.heappop(new_foodtimes)

        eat_time += (now - pre) * leng

        leng -= 1
        pre = now

    new_foodtimes.sort(key=lambda w: w[1])
    return new_foodtimes[(k - eat_time) % leng][1]


# 1
print(solution([3, 1, 2], 5))

# 3
print(solution([4, 2, 3, 6, 7, 1, 6, 8], 16))

# 5
print(solution([4, 2, 3, 6, 7, 1, 6, 8], 27))

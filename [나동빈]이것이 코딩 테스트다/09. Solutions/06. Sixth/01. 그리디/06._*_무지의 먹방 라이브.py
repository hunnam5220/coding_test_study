import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    new_food_times = []
    length = len(food_times)
    for idx in range(length):
        heapq.heappush(new_food_times, [food_times[idx], idx + 1])

    pre = 0
    sum_value = 0

    while sum_value + ((new_food_times[0][0] - pre) * length) < k:
        now = heapq.heappop(new_food_times)[0]
        sum_value += (now - pre) * length
        length -= 1
        pre = now

    new_food_times.sort(key=lambda x: x[1])
    return new_food_times[(k - sum_value) % length][1]


# 1
print(solution([3, 1, 2], 5))

# 3
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))

# 5
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))

import heapq


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    new_food_times = []
    for i in range(1, length + 1):
        heapq.heappush(new_food_times, [food_times[i - 1], i])

    pre, total_times = 0, 0

    while total_times + ((new_food_times[0][0] - pre) * length) <= k:
        now, idx = heapq.heappop(new_food_times)
        total_times += (now - pre) * length
        pre = now
        length -= 1

    new_food_times.sort(key=lambda x: x[1])
    answer = new_food_times[(k - total_times) % length]
    return answer[1]


# 1
print(solution([3, 1, 2], 5))

# 3
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))

# 5
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))

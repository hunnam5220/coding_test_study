import heapq


def solution(food_times, k):
    new_food = []
    if sum(food_times) <= k:
        return -1

    for x in range(1, len(food_times) + 1):
        heapq.heappush(new_food, [food_times[x - 1], x])

    sum_val = 0
    pre = 0
    leng = len(food_times)

    """"""
    while sum_val + ((new_food[0][0] - pre) * leng) <= k:
        now = heapq.heappop(new_food)[0]
        sum_val += (now - pre) * leng

        leng -= 1
        pre = now

    result = sorted(new_food, key=lambda x: x[1])
    return result[(k - sum_val) % leng][1]


# 1
print(solution([3, 1, 2], 5))

# 1
print(solution([8, 6, 4], 15))

# 3
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))

# 5
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))

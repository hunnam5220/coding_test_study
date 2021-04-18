import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    else:
        q = []
        length = len(food_times)
        minus = 0

        for i in range(length):
            heapq.heappush(q, [food_times[i], i + 1])

        while q[0][0] * length < k:
            minus += q[0][0]
            nn = q[0][0]
            k -= nn * length
            heapq.heappop(q)
            length -= 1
            q[0][0] -= minus

        q.sort(key=lambda x: x[1])
        return q[k % length][1]


food_times = [3, 1, 2, 1, 1, 1]
k = 15
print(solution(food_times, k))

# 3
food_times = [4, 2, 3, 6, 7, 1, 5, 8]
k = 16
print(solution(food_times, k))

# 5
food_times = [4, 2, 3, 6, 7, 1, 5, 8]
k = 27
print(solution(food_times, k))

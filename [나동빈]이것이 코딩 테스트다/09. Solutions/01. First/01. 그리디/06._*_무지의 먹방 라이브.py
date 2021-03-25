import heapq


def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    else:
        q = []
        length = len(food_times)
        minus = 0

        for step in range(length):
            heapq.heappush(q, [food_times[step], step + 1])

        while q[0][0] * length < k:
            minus += q[0][0]
            nn = q[0][0]
            k -= nn * length
            heapq.heappop(q)
            length -= 1
            q[0][0] -= minus

        q.sort(key=lambda x: x[1])
        return q[k % length][1]


k, food_times = 28, [3, 10, 9, 11, 8]
print(solution(food_times, k))

k, food_times = 5, [3, 1, 2]
print(solution(food_times, k))

k, food_times = 9, [9, 1]
print(solution(food_times, k))

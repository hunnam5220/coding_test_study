# 시간의 값이 작은 것부터 꺼내야하니까 heapq
# 시간이 작은 순으로 정렬하고 작은 것부터 하나씩 지워나가면 됨
# 정렬하지않고 heapq로 구현해도 됨
import heapq


def solution(food_times, k):
    # food_times 리스트의 합이 k보다 작거나 같으면
    # 더 이상 남을 음식이 없기 때문에 -1 return
    if sum(food_times) <= k:
        return -1

    q = []
    length = len(food_times)
    # 이 새끼 뭐하는 새1끼임? 어따 써먹음?
    minus = 0

    # food_times 의 길이만큼 음식시간과 음식 번호를 넣어준다
    for i in range(length):
        heapq.heappush(q, [food_times[i], i + 1])

    # 힙큐 첫번째 원소의 시간 값과 food_times 배열의 길이를 곱한 값이 k 보다 작으면 반복
    while q[0][0] * length < k:
        # 이전 음식을 다 먹은 시간의 누적값
        minus += q[0][0]

        # 다 먹는 시간을 계산해서 k에서 뺌
        k -= q[0][0] * length

        # 뽑았으니까 길이 조정 다시 해줌
        heapq.heappop(q)
        length -= 1

        # 이전 음식 먹은 시간의 누적값을 뺌
        q[0][0] -= minus

    # 음식 번호순으로 정렬
    q.sort(key=lambda x: x[1])

    # k를 남은 음식 개수로 나눈 나머지 값에 해당하는 리스트의 음식 번호를 return
    return q[k % length][1]


# food_times = [3, 1, 2]
# k = 5
# print(solution(food_times, k))

# 3
food_times = [4, 2, 3, 6, 7, 1, 5, 8]
k = 16
print(solution(food_times, k))

# 5
food_times = [4, 2, 3, 6, 7, 1, 5, 8]
k = 27
print(solution(food_times, k))

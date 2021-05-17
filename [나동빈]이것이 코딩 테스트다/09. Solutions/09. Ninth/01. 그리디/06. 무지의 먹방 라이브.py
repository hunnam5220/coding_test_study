import heapq


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    new_ft = []
    ft_len = len(food_times)
    for step in range(ft_len):
        heapq.heappush(new_ft, [food_times[step], step + 1])

    sv, pre = 0, 0

    while sv + ((new_ft[0][0] - pre) * ft_len) < k:
        ft, fnum = heapq.heappop(new_ft)
        sv += (ft - pre) * ft_len
        ft_len -= 1
        pre = ft

    new_ft.sort(key=lambda x: x[1])
    return new_ft[(k - sv) % ft_len][1]


# 1
print(solution([3, 1, 2], 5))

def solution(nm, balls):
    n, m = nm
    answer = 0
    for x in range(n):
        for y in range(x + 1, n):
            if balls[x] != balls[y]:
                answer += 1
    return answer


# 8
print(solution([5, 3], [1, 3, 2, 3, 2]))

# 25
print(solution([8, 5], [1, 5, 4, 3, 2, 4, 5, 2]))

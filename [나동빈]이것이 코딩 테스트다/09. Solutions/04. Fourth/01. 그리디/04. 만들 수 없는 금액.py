def solution(n, money):
    money.sort()
    answer = 1
    for i in money:
        if i > answer:
            break
        else:
            answer += i
    return answer


print(solution(5, [3, 2, 1, 1, 9]))

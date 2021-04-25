def solution(num):
    result = int(num[0])
    for i in range(1, len(num)):
        if result != 0 and int(num[i]) != 0:
            result *= int(num[i])
        else:
            result += int(num[i])

    return result


print(solution("02984"))
print(solution("567"))

"""
02984

567
"""
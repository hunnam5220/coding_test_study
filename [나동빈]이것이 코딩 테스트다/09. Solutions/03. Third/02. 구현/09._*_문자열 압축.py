def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        comp = ""
        prev = s[0:step]
        cnt = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                cnt += 1
            else:
                if cnt > 1:
                    comp += str(cnt) + prev
                else:
                    comp += prev

                prev = s[j:j+step]
                cnt = 1

        if cnt > 1:
            comp += str(cnt) + prev
        else:
            comp += prev

        answer = min(answer, len(comp))

    return answer


# 7
s = "aabbaccc"
print(solution(s))

# 9
s = "ababcdcdababcdcd"
print(solution(s))

# 8
s = "abcabcdede"
print(solution(s))

# 14
s = "abcabcabcabcdededededede"
print(solution(s))

# 17
s = "xababcdcdababcdcd"
print(solution(s))

# 5
s = "xxxxxxxxxxyyy"
print(solution(s))
def solution(s):
    length = len(s)
    answer = 1e9
    for k in range(1, length + 1):
        check = s[0:k]
        temp_str = s[0:k]
        cnt = 1

        for j in range(k, length + 1, k):
            if s[j:j + k] == check:
                cnt += 1
            else:
                if cnt > 1:
                    temp_str += str(cnt)
                    cnt = 1
                temp_str += s[j:j + k]
                check = s[j:j + k]

        answer = min(answer, len(temp_str))

    return answer


# 7
print(solution("aabbaccc"))

# 9
print(solution("ababcdcdababcdcd"))

# 8
print(solution("abcabcdede"))

# 14
print(solution("abcabcabcabcdededededede"))

# 17
print(solution("xababcdcdababcdcd"))

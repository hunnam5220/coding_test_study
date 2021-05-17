def solution(s):
    s_len = len(s)
    answer = 1e9

    for i in range(1, s_len + 1):
        string = s[:i]
        k = s[:i]
        start = i
        cnt = 1
        tmp_len = i

        for j in range(i + i, s_len + 1, i):
            x = s[start:j]
            if x == k:
                cnt += 1
            else:
                if cnt > 1:
                    string += str(cnt)
                    cnt = 1

                k = x
                string += k
            start += i
            tmp_len += i

        if cnt > 1:
            string += str(cnt)

        if tmp_len != s_len:
            temp = s[tmp_len:]
            string += temp

        answer = min(len(string), answer)
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
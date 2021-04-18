def solution(s):
    length = len(s)
    answer = length

    for cut in range(1, length // 2 + 1):
        start = 0
        end = cut

        key = s[start:end]
        temp_str = key
        cnt = 1

        for i in range(1, length // cut):
            start += cut - 1
            end += cut - 1
            next_key = s[i + start: i + end]
            if next_key == key:
                cnt += 1
            else:
                if cnt != 1:
                    temp_str += str(cnt)
                    cnt = 1
                key = next_key
                temp_str += key

            if next_key == '' or i == length // cut - 1:
                if cnt != 1:
                    temp_str += str(cnt)

        if length % cut != 0:
            k = length % cut
            temp_str += s[-k:]

        answer = min(answer, len(temp_str))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

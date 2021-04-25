def solution(string):
    c = [False, False]
    answer = 1e9

    for chk in range(2):
        cnt = 0
        for l in string:
            if int(l) == chk and not c[chk]:
                c[chk] = True
                cnt += 1
            elif int(l) != chk and c[chk]:
                c[chk] = False
        answer = min(answer, cnt)

    return answer


print(solution("0001100"))
print(solution("01001100"))
print(solution("01100110101010100"))
print(solution("010011000001100100"))
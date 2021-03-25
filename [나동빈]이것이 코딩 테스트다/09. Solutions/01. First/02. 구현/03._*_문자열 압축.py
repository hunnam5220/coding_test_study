def solution(s):
    answer = len(s)

    for step in range(1, (len(s)//2) + 1):
        tmp = s

        if step == 1:
            cnt = 1
            tmp = list(tmp)
            now = tmp.pop(0)
            tmp.reverse()
            result = now

            while tmp:
                k = tmp.pop()
                if k != now:
                    if cnt > 1:
                        result += str(cnt) + k
                        now = k
                    else:
                        result += k
                        now = k
                    cnt = 1

                else:
                    cnt += 1

            if now == k and cnt > 1:
                result += str(cnt)

            answer = len(result)

        else:
            chk_len = len(tmp)
            tmp = list(tmp)
            arr, start, end = [], 0, step

            while chk_len >= 1:
                arr.append(''.join(tmp[start:end]))
                chk_len -= step
                start += step
                end += step

            arr.reverse()
            now = arr.pop()
            result = ''
            cnt = 1
            while arr:
                tmp = arr.pop()
                if now != tmp:
                    if cnt < 2:
                        result += now
                        now = tmp
                    else:
                        result += now + str(cnt)
                        now = tmp
                        cnt = 1
                else:
                    cnt += 1

            if now == tmp and cnt > 1:
                result += now + str(cnt)
            else:
                result += now

            if len(result) < answer:
                answer = len(result)

    return answer


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print(solution('x'))


"""
"aabbaccc"                      7
"ababcdcdababcdcd"	            9
"abcabcdede"	                8
"abcabcabcabcdededededede"	    14
"xababcdcdababcdcd"	            17
"""
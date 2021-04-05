from sys import stdin
from itertools import permutations
from collections import deque

n = int(stdin.readline().rstrip())
arr = list(stdin.readline().rstrip().split())
arr.sort()
cal = []
d = {0: '+', 1: '-', 2: '*', 3: '/'}
result = []


def get_cal_string(prod):
    cal_string = ''
    leng = len(arr)
    for s in range(leng):
        cal_string += arr[s]
        if s < (leng - 1):
            cal_string += prod[s]

    return cal_string


def get_calc_val(cal_st):
    q = deque(list(cal_st))
    val, tmp, code = None, None, None
    while q:
        s = q.popleft()

        if s.isdigit() and val is None:
            val = int(s)

        elif not s.isdigit():
            code = s

        elif s.isdigit() and val is not None:
            tmp = int(s)

        if val is not None and tmp is not None and code is not None:
            if code == '+':
                val += tmp
            elif code == '-':
                val -= tmp
            elif code == '*':
                val *= tmp
            elif code == '/':
                if val < 0 and tmp > 0:
                    val = abs(val) // tmp * -1
                elif tmp == 0:
                    val = 0
                else:
                    val //= tmp

            tmp, code = None, None

    return val


for x, i in zip(list(map(int, stdin.readline().split())), range(4)):
    for _ in range(x):
        cal.append(d[i])

cal_prod = list(permutations(cal, len(cal)))

max_val = 0
min_val = int(1e9)

for step in range(len(cal_prod)):
    calc_string = get_cal_string(cal_prod[step])
    val = get_calc_val(calc_string)

    if val < min_val:
        min_val = val

    if val > max_val:
        max_val = val

print(max_val)
print(min_val)
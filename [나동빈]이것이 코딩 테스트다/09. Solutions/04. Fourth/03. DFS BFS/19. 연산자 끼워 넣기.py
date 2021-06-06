from sys import stdin
from itertools import permutations

n = int(stdin.readline().rstrip())
num = list(map(int, stdin.readline().split()))
cal_ = list(map(int, stdin.readline().split()))
gi = ['+', '-', '*', '/']
cg = []
vmax = -1e9
vmin = 1e9


def calculation(sign, num):
    global vmax, vmin
    calc_num = num[0]

    for idx in range(1, len(num)):
        if sign[idx - 1] == '+':
            calc_num += num[idx]

        elif sign[idx - 1] == '-':
            calc_num -= num[idx]

        elif sign[idx - 1] == '*':
            calc_num *= num[idx]

        elif sign[idx - 1] == '/':
            if num[idx] < 0 or calc_num < 0:
                calc_num = abs(calc_num) // abs(num[idx]) * -1
            else:
                calc_num //= num[idx]

    vmax = max(vmax, calc_num)
    vmin = min(vmin, calc_num)


for i in range(4):
    cg.extend([gi[i]] * cal_[i])


for sign in list(set(permutations(cg, n - 1))):
    calculation(sign, num)

print(vmax)
print(vmin)
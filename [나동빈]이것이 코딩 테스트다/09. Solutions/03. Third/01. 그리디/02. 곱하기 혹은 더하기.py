from sys import stdin

num = list(stdin.readline().rstrip())
result = int(num[0])

for x in range(1, len(num)):
    if result != 0 and num[x] != 0:
        result *= int(num[x])
    else:
        result += int(num[x])

print(result)
"""
02984

567
"""
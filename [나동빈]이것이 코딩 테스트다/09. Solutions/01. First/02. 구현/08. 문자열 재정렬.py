from sys import stdin

a = list(stdin.readline().rstrip())
a.sort()
result = 0

for step in range(len(a)):
    try:
        result += int(a[step])
    except:
        a = a[step:]
        break

print(''.join(a) + str(result))


"""
K1KA5CB7

AJKDLSI412K4JSJ9D
"""
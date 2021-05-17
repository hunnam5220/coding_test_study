from sys import stdin
string = list(stdin.readline().rstrip())
string.sort()
idx = 0

for x in string:
    if not x.isalpha():
        idx += 1
    else:
        break

print(''.join(string[idx:]) + str(sum(list(map(int, string[:idx])))))


"""
K1KA5CB7
AJKDLSI412K4JSJ9D
"""
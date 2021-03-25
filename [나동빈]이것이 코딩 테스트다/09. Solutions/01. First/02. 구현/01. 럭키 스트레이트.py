from sys import stdin
num = stdin.readline().rstrip()
a, b = num[:len(num)//2], num[len(num)//2:]
if sum(list(map(int, a))) == sum(list(map(int, b))):
    print("LUCKY")
else:
    print("READY")
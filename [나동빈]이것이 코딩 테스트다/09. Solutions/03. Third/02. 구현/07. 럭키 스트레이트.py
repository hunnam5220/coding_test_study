from sys import stdin

string = stdin.readline().rstrip()
num1, num2 = list(map(int, string[:len(string)//2])), list(map(int, string[len(string)//2:]))

if sum(num1) == sum(num2):
    print("LUCKY")

else:
    print("READY")
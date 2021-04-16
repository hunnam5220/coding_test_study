from sys import stdin

st = list(map(int, stdin.readline().rstrip()))
st.sort()
start = st[0]

for i in range(1, len(st)):
    if start * st[i] == 0 or start * st[i] == start:
        start += st[i]
    else:
        start *= st[i]

print(start)

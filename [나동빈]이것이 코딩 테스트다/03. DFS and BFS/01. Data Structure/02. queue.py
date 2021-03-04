from collections import deque as dq

queue = dq()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
# 최상단 원소부터 출력하기 위해 역순으로 변경
queue.reverse()
# 최상단 원소부터 출력
print(queue)

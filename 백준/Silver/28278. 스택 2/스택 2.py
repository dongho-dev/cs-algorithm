from collections import deque
import sys

dq = deque()

n = int(input())

for x in range(0, n):
    x = list(map(int, sys.stdin.readline().split()))

    if len(x) > 0:
        if x[0] == 1:
            if len(x) > 1:
                dq.append(x[1])

        elif x[0] == 2:
            if len(dq) == 0:
                print(-1)
            else: 
                print(dq.pop())

        elif x[0] == 3:
            print(len(dq))

        elif x[0] == 4:
            if len(dq) == 0:
                print(1)
            else: 
                print(0)

        elif x[0] == 5:
            if len(dq) == 0:
                print(-1)
            else: 
                n = dq.pop()
                print(n)
                dq.append(n)

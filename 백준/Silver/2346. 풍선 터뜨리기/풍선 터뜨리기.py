from collections import deque
import sys

dq = deque() 
N = int(input())
ballon = deque(enumerate(map(int, sys.stdin.readline().split())))

while ballon:
    cur, paper = ballon.popleft()
    dq.append(cur + 1)
        
    if paper > 0:
        ballon.rotate(-(paper - 1))
    elif paper < 0:
        ballon.rotate(-paper)

for i in range(len(dq)):
    print(dq[i], end=' ')





import sys
from collections import deque

N, M = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))
result = 0

dq = deque(range(1, N + 1))

def moveToLeft():
    temp = dq.popleft()
    dq.append(temp)

def moveToRight():
    temp = dq.pop()
    dq.appendleft(temp)

def countLeftMove(num):
    leftCount = 0
    while dq[0] != num:
        moveToLeft()
        leftCount += 1
    return leftCount

def countRightMove(num):
    rightCount = 0
    while dq[0] != num:
        moveToRight()
        rightCount += 1
    return rightCount

def find(num):
    leftMoves = countLeftMove(num)
    for _ in range(leftMoves):
        moveToRight()  

    rightMoves = countRightMove(num)
    for _ in range(rightMoves):
        moveToLeft()  

    if leftMoves > rightMoves:
        for _ in range(rightMoves):
            moveToRight()
        return rightMoves
    for _ in range(leftMoves):
        moveToLeft() 
    return leftMoves

for num in seq:
    result += find(num)
    dq.popleft()

print(result)

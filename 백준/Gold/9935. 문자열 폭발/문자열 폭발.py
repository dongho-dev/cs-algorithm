import sys
from collections import deque 

# 입력 처리
str1 = sys.stdin.readline().strip()
tnt1 = sys.stdin.readline().strip()

# 폭발 처리
stack = []
for i in str1:
    stack.append(i)
    if len(stack) >= len(tnt1) and ''.join(stack[-len(tnt1):]) == tnt1:
        del stack[-len(tnt1):]
    
# 출력
stack = ''.join(stack)
if stack:
    print(stack)
else:
    print("FRULA")

import sys

n = int(sys.stdin.readline())
stack = []
result = 0

for _ in range(n):
    h = int(sys.stdin.readline())
    while stack and stack[-1] <= h:
        stack.pop()
    result += len(stack)
    stack.append(h)

print(result)
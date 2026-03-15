import sys
from collections import deque

# 입력 처리
N, L = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

# 최소값 D 처리
D = []
dq = deque()

for i in range(N):
    if dq and dq[0] < i - L + 1:
        dq.popleft()

    while dq and A[dq[-1]] > A[i]: 
        dq.pop()

    dq.append(i)

    D.append(A[dq[0]])

# 출력 처리
print(' '.join(map(str, D)))
import sys

# 첫째 줄에 두 정수 N, M이 주어진다. 
N, M = map(int, sys.stdin.readline().strip().split())

# 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.
A = []
for _ in range(N): # 1 ≤ N ≤ 100,000
    i = int(sys.stdin.readline().strip())
    A.append(i)

A.sort()

en = 0
minimum = float('inf')

for st in range(N):
    while en < N and (A[en] - A[st]) < M: 
        en += 1

    if en == N: 
        break

    if (A[en] - A[st]) == M:
        minimum = M
        break

    minimum = min(minimum, (A[en] - A[st]))

# 첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 
# 항상 차이가 M 이상인 두 수를 고를 수 있다.
print(minimum)
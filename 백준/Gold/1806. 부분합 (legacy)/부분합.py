import sys

# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다.
N, S = map(int, sys.stdin.readline().strip().split())

# 둘째 줄에는 수열이 주어진다. 
# 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000 이하의 자연수이다.
A = list(map(int, sys.stdin.readline().strip().split()))    

minimum = float('inf')
en = 0
partSum = A[0]

for st in range(N):    
    while en < N and partSum < S:
        en += 1
        if en != N:
            partSum += A[en]
    
    if en == N:
        break
    
    minimum = min((en - st + 1), minimum)
    partSum -= A[st]
        
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 
# 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
if minimum == float('inf'):
    print(0)
else:
    print(minimum)

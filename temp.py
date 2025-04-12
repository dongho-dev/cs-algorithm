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


'''
st0, en0, A0 
st1, en1, A0-A1

# 1806 부분합

시간제한 0.5초, N 개수가 10만개이므로 O(N^2)는 시간 초과.
O(N log N) 이하로 로직 작성.

10000 이하의 자연수로 이루어진 길이 N 수열 주어짐.
이 수열에서 연속된 수들의 부분합 중에 합이 S 이상인 것들 중
가장 짧은 부분합의 길이를 구해야 함.

# 입력 테스트 통과
print("입력 테스트: ", N, S)
print(A)

연속된 수의 부분합 중 S보다 크면서 최소값을 구해야 하니 
오름차순으로 수열을 정렬한다. 

반복문 루프를 돌면서, S 이상인 값을 만날 때까지 반복.
S 이상인 값이 있으면 만나는 순간 바로 탈출.

S보다 큰 값이 없으면 2개, 3개 ... 길이 늘리면서 부분합 탐색.

en = 0, 1, 2 ....
for st in range(N):
        partSum = 0

        for st in range(en):
            partSum += A[st]        
    
        if partSum > S:
            minimum = min(partSum, minimum)

        if partSum == S:
            minimum = S
            break
    
        en += 1

위 코드를 처음 짜고, 아래로 합치니 시간 초과가 예상되는 코드가 나온다.   
불가능하다면 0을 출력해야 한다는 건, 최악의 경우 전체 탐색을 해야 할 수도.

for en in range(N):
    for st in range(N):
        partSum = 0

        for st in range(en):
            partSum += A[st]        
    
        if partSum > S:
            minimum = min(partSum, minimum)

        if partSum == S:
            minimum = S
            break
    
        en += 1

        
! '연속'된 수의 부분합이어서 정렬해서는 안되는 것이었음.
수 고르기(2230) 문제는 두 수를 자유롭게 골라고 되며,
연속하지 않아도 되기에 정렬이 가능했던 것. 착각하지 말아야 함.

 
'''
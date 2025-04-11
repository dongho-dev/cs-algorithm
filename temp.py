import sys

# 첫째 줄에 두 정수 N, M이 주어진다. 
N, M = map(int, sys.stdin.readline().strip().split())

# 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.
A = []
for _ in range(N): # 1 ≤ N ≤ 100,000
    input = int(sys.stdin.readline().strip())
    A.append(input)

minimum = 0 # 0 ≤ M ≤ 2,000,000,000


# 입력 테스트
print("입력 테스트")
print(N, M)
print(A)

# 첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 
# 항상 차이가 M 이상인 두 수를 고를 수 있다.
print(minimum)


'''
# 2230 수 고르기

두 수 A, B를 고르는데, (같을 수도 있음)
이 차이가 M 이상이면서 가장 작은 경우를 구해야 함.

수열이 1~5까지 있으면
M이 3이라고 가정하면

1, 4 / 1, 5 / 2, 5 3가지 경우가 차이가 M(3) 이상이다.
그중에 가장 작은 경우 (1,4 / 2,5) 의 차이를 출력해야 함. 여기선 3

'''
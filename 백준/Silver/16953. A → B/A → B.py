import sys

# 입력 처리
A, B = map(int, sys.stdin.readline().split())

# A -> B 연산 처리
minimum = 0

while B > A:
    if B >= 11 and B % 10 == 1:
        minimum += 1
        B = (B - 1) / 10
    else:
        minimum += 1
        B = B / 2

# 출력 처리
if minimum == 0 or A != B:
    print(-1)
else:
    print(minimum + 1)
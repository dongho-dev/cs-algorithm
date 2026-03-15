import sys
import re

# 입력 처리
S = sys.stdin.readline().strip()

# 최소값 탐색 처리
result = 0
minus = False
S = re.split(r'([+\-])', S)

for i in S:
    if i == '+':
        continue
    elif i == '-':
        minus = True
    else:
        if minus:
            result -= int(i)
        else:
            result += int(i)
# 출력 처리
print(result)
import sys
from collections import deque

# 입력 처리
T = int(sys.stdin.readline()) # T < 100
for _ in range(T): 
    P = list(sys.stdin.readline().strip()) # 1 <= len(p) <= 100000
    N = int(sys.stdin.readline().strip()) # 0 <= N <= 100000
    X = sys.stdin.readline().strip() # 1 <= X <= 100
    # len(p) + N <= 700000
    
    dq = deque()
    X = X.strip('[]')
    if X:
        num = X.split(',')
        for i in num:
            dq.append(i)

    # 함수 처리
    error = False
    reverse = False

    for j in P:
        if j == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True    
        else:
            if dq:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                error = True
                break

    if not error and reverse:
        dq.reverse()

    # 출력 처리
    if error:
        print("error")
    else:
        result = "[" + ",".join(dq) + "]"
        print(result)

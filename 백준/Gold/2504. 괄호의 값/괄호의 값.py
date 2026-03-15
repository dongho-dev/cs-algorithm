import sys

# 입력 처리
S = list(sys.stdin.readline().strip())

# 문자열 값 계산
stack = []
invalidStr = False
result = 0

for i in S:
    if i == '(':
        stack.append(i)
    elif i == '[':
        stack.append(i)
    elif i == ')':
        if stack:
            cur = 0
            while stack and isinstance(stack[-1], int):
                cur += stack.pop()
            if not stack or stack[-1] != '(':
                invalidStr = True
                break
            stack.pop()
            if cur == 0:
               stack.append(2)
            else:
                stack.append(cur * 2)
        else:
            invalidStr = True
            break     
                
    elif i == ']':
        if stack:
            cur = 0
            while stack and isinstance(stack[-1], int):
                cur += stack.pop()
            if not stack or stack[-1] != '[':
                invalidStr = True
                break
            stack.pop()
            if cur == 0:
               stack.append(3)
            else:
                stack.append(cur * 3)
        else:
            invalidStr = True
            break

for i in stack:
    if isinstance(i, int):
        result += i
    else:
        invalidStr = True
        break

# 출력 처리
if invalidStr:
    print(0)
else:
    print(result)

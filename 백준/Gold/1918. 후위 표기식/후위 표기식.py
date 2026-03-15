import sys

# 입력 처리
S = list(sys.stdin.readline().strip())

# 후위 표기식 처리ㅣ
stack = []
result = []

for i in S:
    if i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result.append(stack.pop())
        stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        if stack:
            stack.pop()
    else:
        result.append(i)
    
while stack:
    result.append(stack.pop())

# 출력 처리
print(''.join(result))

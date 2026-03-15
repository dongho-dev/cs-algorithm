import sys

# 입력 처리
string = list(sys.stdin.readline().strip())
N = len(string)
cursor = N
M = int(sys.stdin.readline().strip()) 

# 명령어 처리
stack1 = string
stack2 = []
for _ in range(M):
    command = sys.stdin.readline().strip()
    if command == "L":
        if stack1:
            move = stack1.pop()
            stack2.append(move)
    elif command == "D":
        if stack2:
            move = stack2.pop()
            stack1.append(move)
    elif command == "B":
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[-1])

# 출력 처리
result = ''.join(stack1 + stack2[::-1])
print(result)

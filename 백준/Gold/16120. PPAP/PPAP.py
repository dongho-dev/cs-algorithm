import sys

# 입력 처리
S = list(sys.stdin.readline().strip())

# PPAP 문자열 처리
ppap = False
stack = []
pcount = 0

for i in S:
    stack.append(i)
    if len(stack) >= 4:
        check = [] 
        for _ in range(4):
            check.append(stack.pop())

        if ''.join(check) == "PAPP":
            stack.append("P")
        else:
            while check:
                stack.append(check.pop())

if stack:
    if len(stack) == 1 and stack[-1] == "P":
        ppap = True

# 출력 처리
if ppap:
    print("PPAP")
else:
    print("NP")
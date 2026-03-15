import sys

# 입력 처리
S = list(sys.stdin.readline().strip('\n'))

# 태그 처리
vocaStack = []
result = []
tag = False

for i in S:
    if i == "<":
        tag = True
        while vocaStack:
            result.append(vocaStack.pop())
        result.append(i)
    elif i == ">":
        tag = False
        result.append(i)
    elif tag:
        result.append(i)
    else:
        if i == " ":
            while vocaStack:
                result.append(vocaStack.pop())
            result.append(i)    
        else:
            vocaStack.append(i)

while vocaStack:
    result.append(vocaStack.pop())

# 출력 처리
print(''.join(result))

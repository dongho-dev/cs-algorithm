import sys

# 입력 처리
N = int(sys.stdin.readline())
histo = []
for n in range(N):
    i = int(sys.stdin.readline())
    histo.append((n, i))

# 가장 큰 직사각형 찾기
largest = 0
stack = []
width = 0
area = 0

for i, j in histo:
    if not stack:
        stack.append((i, j))
    else:
        if j >= stack[-1][1]:
            stack.append((i, j))
        else:
            while stack and j <= stack[-1][1]:
                topindex, top = stack.pop()
                if stack:
                    width = i - stack[-1][0] - 1
                else:
                    width = i

                area = top * width
                if area > largest:
                    largest = area

            stack.append((i, j))

if stack:
    while stack:
        topindex, top = stack.pop()
        if stack:
            width = N - stack[-1][0] - 1
        else:
            width = N

        area = top * width
        if area > largest:
            largest = area

# 출력 처리
print(largest)
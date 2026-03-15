import sys

# 0을 입력으로 받을 때까지 반복해서 입력
while True:
    data = sys.stdin.readline().strip()
    
    if data == '0':
        break
    
    nums = list(map(int, data.split()))
    
    n = nums[0]
    heights = nums[1:]
    
    stack = []
    max_area = 0

    # 히스토그램의 높이를 차례로 처리
    for i in range(n):
        # 현재 높이보다 큰 직사각형들을 처리
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            if stack:
                area = heights[top] * (i - stack[-1] - 1)
            else:
                area = heights[top] * i
            max_area = max(max_area, area)
        stack.append(i)

    # 남아 있는 직사각형 처리
    while stack:
        top = stack.pop()
        if stack:
            area = heights[top] * (n - stack[-1] - 1)
        else:
            area = heights[top] * n
        max_area = max(max_area, area)

    print(max_area)

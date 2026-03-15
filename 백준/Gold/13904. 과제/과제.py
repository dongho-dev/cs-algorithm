import sys

# 과제 입력 받기
N = int(sys.stdin.readline())
quest = []
maxDay = 0

for _ in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())

    # 점수 기준으로 간편하게 정렬하기 위해 w d 순으로 저장.
    quest.append((w, d))
    maxDay = max(maxDay, d)

# 점수 기준 내림차순으로 정렬
quest.sort(reverse=True)

# 날짜별 과제 체크용 배열
visited = [False] * (maxDay + 1)
totalScore = 0

for w, d in quest:
    # 역순으로 마감일부터 순차적으로 탐색해서 빈 날에 과제 저장
    for day in range(d, 0, -1):
        if not visited[day]:
            visited[day] = True
            totalScore += w
            break

print(totalScore)

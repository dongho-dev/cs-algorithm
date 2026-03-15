import sys

a = []

n = int(input())
for i in range(0, n):
  x, y = map(int, sys.stdin.readline().split()) 
  a.append([x, y])

a.sort(key=lambda p: (p[0], p[1]))

for i in a:
  print(i[0], i[1])

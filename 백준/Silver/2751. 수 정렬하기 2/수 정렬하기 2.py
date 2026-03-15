import sys

n = int(input())
ilist = []

for i in range(0, n):
  a = int(sys.stdin.readline())
  ilist.append(a)

ilist.sort()
for x in ilist:
  print(x)
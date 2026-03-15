import sys

N = int(input())
voca = []
for i in range(0, N):
  voca.append(input())

voca = sorted(set(voca), key=lambda x: (len(x), x))
for x in voca:
    print(x)
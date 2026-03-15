import sys

def square(x):
  return x * x

while True:
  n = list(map(int, sys.stdin.readline().split()))
  if n == [0, 0, 0]:
    break;
  else:
    n.sort()
    if square(n[0]) + square(n[1]) == square(n[2]):
      print("right")
    else:
      print("wrong")
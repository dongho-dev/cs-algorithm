import sys

def bSearchRecursive(a, d, first, last):
    if first > last:
        print("0")
        return
    mid = (first + last) // 2
    if a[mid] == d:
        print("1")
        return
    elif a[mid] > d:
        return bSearchRecursive(a, d, first, mid - 1)
    else:
        return bSearchRecursive(a, d, mid + 1, last)

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
B = list(map(int, sys.stdin.readline().split()))

for i in range(0, M):
  bSearchRecursive(A, B[i], 0, len(A) - 1)

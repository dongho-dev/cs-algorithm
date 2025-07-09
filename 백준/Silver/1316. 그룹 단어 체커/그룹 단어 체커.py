import sys

def is_group(word: str) -> bool:
    seen = set()
    prev = ''
    for ch in word:
        if ch != prev:
            if ch in seen:
                return False
            seen.add(ch)
            prev = ch
    return True

N = int(sys.stdin.readline())
count = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    if is_group(word):
        count += 1
print(count)

def mutiple(a, b, c):
    if b == 0: return 1
    if b == 1: return a % c

    if b % 2 == 0:
        half = mutiple(a, b // 2, c)
        return (half * half) % c
    else:
        half = mutiple(a, (b - 1) // 2, c)
        return (half * half * a) % c

a, b, c = map(int, input().split())

result = mutiple(a, b, c)
print(result)
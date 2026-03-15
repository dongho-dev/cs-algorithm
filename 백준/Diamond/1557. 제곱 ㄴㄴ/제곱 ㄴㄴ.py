import sys

def precompute_mu(limit):
    mu = [1] * limit
    is_prime = [True] * limit
    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i, limit, i):
                is_prime[j] = False
                mu[j] *= -1
            for j in range(i * i, limit, i * i):
                mu[j] = 0
    return mu

# 최대 필요한 뮤비우스 함수 값을 미리 계산합니다.
MAX_LIMIT = int((2 * 1e9) ** 0.5) + 2  # 최대 N은 2e9로 설정
mu = precompute_mu(MAX_LIMIT)

def count_square_free(N):
    m = int(N ** 0.5) + 1
    total = 0
    for i in range(1, m):
        if mu[i]:
            total += mu[i] * (N // (i * i))
    return total

def main():
    K = int(sys.stdin.readline())
    left = 1
    right = 2 * K  # 탐색 범위 설정
    while left < right:
        mid = (left + right) // 2
        cnt = count_square_free(mid)
        if cnt < K:
            left = mid + 1
        else:
            right = mid
    print(left)

if __name__ == "__main__":
    main()

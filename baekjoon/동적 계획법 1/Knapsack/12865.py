import sys
input = sys.stdin.readline


def solution(N, K, items):
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        weight, value = map(int, items[i-1])
        for j in range(1, K+1):
            if weight <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][K])


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    items = [list(map(int, input().strip().split())) for _ in range(N)]
    solution(N, K, items)

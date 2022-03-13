import sys
input = sys.stdin.readline


def solution(N, K, items):
    dp = [0 for _ in range(K+1)]
    for i in range(0, N):
        for j in range(K, 0, -1):
            if items[i][0] <= j:
                dp[j] = max(dp[j], dp[j-items[i][0]]+items[i][1])

    print(dp[K])


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    items = []
    for _ in range(N):
        items.append(list(map(int, input().strip().split())))
    solution(N, K, items)

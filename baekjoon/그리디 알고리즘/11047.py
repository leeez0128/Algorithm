import sys
input = sys.stdin.readline


def solution(N, K, coins):
    total = 0
    for i in range(N-1, -1, -1):
        needs = K // coins[i]
        if needs > 0:
            K = K - needs * coins[i]
            total += needs
            if K == 0:
                print(total)
                return


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    coins = []
    for _ in range(N):
        coins.append(int(input().strip()))
    solution(N, K, coins)

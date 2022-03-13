# nCk using DP, pascal
import sys
input = sys.stdin.readline


def solution(N, K):
    pascal = [[0], [1, 1], [1, 2, 1]]
    
    if N > 2:
        for n in range(3, N+1):
            pascal.append([1] * (n+1))
            for j in range(1, n):
                pascal[n][j] = pascal[n-1][j-1] + pascal[n-1][j]

    print(pascal[N][K] % 10007)


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N, K)

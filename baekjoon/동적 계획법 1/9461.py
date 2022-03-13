import sys
input = sys.stdin.readline


def solution(N):
    dp = [1 for _ in range(N+1)]

    if N <= 3:
        print(dp[N])
        return
    else:
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[N])


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        solution(int(input().strip()))

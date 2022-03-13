import sys, math
input = sys.stdin.readline


def solution(N, K):
    result = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))

    print(result % 10007)


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N, K)

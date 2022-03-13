import sys
input = sys.stdin.readline


def solution(N, K):
    up, down = 1, 1
    for i in range(K):
        up *= (N-i)
        down *= (i+1)

    print(int(up / down))


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N, K)

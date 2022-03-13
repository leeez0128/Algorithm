import sys
input = sys.stdin.readline


def solution(N):
    for i in range(1, N+1):
        print(i)


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
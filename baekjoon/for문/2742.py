import sys
input = sys.stdin.readline


def solution(N):
    for i in range(N, 0, -1):
        print(i)


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)

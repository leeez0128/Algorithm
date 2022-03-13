import sys
input = sys.stdin.readline


def solution(N):
    for i in range(9):
        print(N, "*", i+1, "=", N*(i+1))


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)

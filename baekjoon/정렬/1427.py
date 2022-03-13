import sys
input = sys.stdin.readline


def solution(N):
    N = sorted(N, reverse=True)
    for num in N:
        print(num, end="")


if __name__ == '__main__':
    N = input().strip()
    solution(N)

import sys
input = sys.stdin.readline


def solution(N):
    count = 0
    for num in range(666, sys.maxsize):
        if '666' in str(num):
            count += 1
        if count == N:
            print(num)
            return


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
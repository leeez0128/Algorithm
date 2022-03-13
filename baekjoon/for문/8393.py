import sys
input = sys.stdin.readline


def solution(n):
    sum = 0
    for i in range(n, 0, -1):
        sum += i
    print(sum)


if __name__ == '__main__':
    n = int(input().strip())
    solution(n)

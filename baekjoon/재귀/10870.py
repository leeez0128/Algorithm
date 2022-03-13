import sys
input = sys.stdin.readline


def solution(n):
    if n <= 1:
        return n
    return solution(n-1) + solution(n-2)


if __name__ == '__main__':
    n = int(input().strip())
    print(solution(n))

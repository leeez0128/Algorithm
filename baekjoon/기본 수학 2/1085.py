import sys
input = sys.stdin.readline


def solution(x, y, w, h):
    print(min(x, y, w-x, h-y))


if __name__ == '__main__':
    x, y, w, h = map(int, input().strip().split())
    solution(x, y, w, h)

import sys
input = sys.stdin.readline


def solution(a, b, c):
    triangle = [a, b, c]
    large = max(a, b, c)
    triangle.remove(large)
    if large**2 == triangle[0]**2 + triangle[1]**2:
        print("right")
    else:
        print("wrong")


if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().strip().split())
        if a == 0 and b == 0 and c == 0:
            sys.exit(0)
        else:
            solution(a, b, c)

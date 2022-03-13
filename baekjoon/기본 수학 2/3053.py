import sys
import math
input = sys.stdin.readline


def solution(R):
    print("{:.6f}".format((R**2)*math.pi))
    print("{:.6f}".format((R**2)*2))


if __name__ == '__main__':
    R = int(input().strip())
    solution(R)

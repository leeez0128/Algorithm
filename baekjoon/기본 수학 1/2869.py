import sys
import math
input = sys.stdin.readline


def solution(A, B, V):
    day = (V - B) / (A - B)
    print(math.ceil(day))


if __name__ == '__main__':
    A, B, V = map(int, input().strip().split())
    solution(A, B, V)

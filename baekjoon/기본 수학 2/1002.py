import sys
import math
input = sys.stdin.readline


def solution(x1, y1, r1, x2, y2, r2):
    core_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if core_distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) < core_distance < r1 + r2:
        print(2)
    elif core_distance == r1 + r2 or core_distance == abs(r1-r2):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
        solution(x1, y1, r1, x2, y2, r2)

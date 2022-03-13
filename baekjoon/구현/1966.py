import sys
from collections import deque
input = sys.stdin.readline


def solution(M, importance):
    out = 1
    while importance:
        _max = max(importance)
        front = importance.popleft()
        M -= 1

        if _max == front:
            if M < 0:
                print(out)
                break
            out += 1
        else:
            importance.append(front)
            if M < 0 :
                M = len(importance) - 1


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        importance = deque(list(map(int, input().strip().split())))
        solution(M, importance)

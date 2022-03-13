import sys
from collections import deque
input = sys.stdin.readline


def solution(N, queue):
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[-1])


if __name__ == '__main__':
    N = int(input().strip())
    queue = deque()
    for i in range(1, N+1):
        queue.append(i)
    solution(N, queue)

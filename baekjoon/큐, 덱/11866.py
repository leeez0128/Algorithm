import sys
from collections import deque
input = sys.stdin.readline


def solution(N, K):
    queue = deque()
    for i in range(1, N+1):
        queue.append(str(i))
    
    print("<", end="")
        
    while len(queue) != 1:
        for _ in range(K-1):
            queue.append(queue.popleft())
        print(queue.popleft(), ", ", sep="", end="")
    
    print(queue[-1], ">", sep="")


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N, K)

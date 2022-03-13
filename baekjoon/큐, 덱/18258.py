import sys
from collections import deque
input = sys.stdin.readline


def solution(N):
    queue = deque()
    for _ in range(N):
        order = input().strip()
        if len(order.split(" ")) > 1:
            queue.append(order.split(" ")[1])
        elif order == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif order == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif order == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif order == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif order == 'size':
            print(len(queue))
            
            
if __name__ == '__main__':
    N = int(input().strip())
    solution(N)

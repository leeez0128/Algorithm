import sys
from collections import deque
input = sys.stdin.readline


def order(queue, string):
    if len(string.split(" ")) > 1:
        if string.split(" ")[0] == 'push_front':
            queue.appendleft(string.split(" ")[1])
        else:
            queue.append(string.split(" ")[1])
            
    elif string == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif string == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
            
    elif string == 'size':
        print(len(queue))
        
    elif string == 'empty':
        if queue:
            print(0)
        else:
            print(1)
        
    elif string == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
        
    elif string == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


def solution(N):
    queue = deque()
    for _ in range(N):
        order(queue, input().strip())
        

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
import sys
from collections import deque
input = sys.stdin.readline


def solution(n, m, pos):
    queue = deque([i for i in range(1, n+1)])
    result = 0 
    
    for num in pos:
        while True:
            if queue[0] == num:
                queue.popleft()
                break
            else:
                if queue.index(num) < len(queue)/2:
                    while queue[0] != num:
                        queue.append(queue.popleft())  
                        result += 1
                else:
                    while queue[0] != num:
                        queue.appendleft(queue.pop())  
                        result += 1
    print(result)

    
if __name__=='__main__':
    n, m = map(int, input().strip().split())
    pos = list(map(int, input().strip().split()))
    solution(n, m, pos)
    

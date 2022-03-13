import sys, heapq
input = sys.stdin.readline


result = []
def solution(x):
    if x == 0:
        if len(result) == 0:
            print(0)
        else:
            print(heapq.heappop(result)[1])
    else:
        heapq.heappush(result, (abs(x), x))
        
    
if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        solution(int(input().strip()))
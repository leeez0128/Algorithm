import sys, heapq
input = sys.stdin.readline

leftHeap = []
rightHeap = []
def solution(x):
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -x)
    else:
        heapq.heappush(rightHeap, x)
    
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)
    
    print(-leftHeap[0])


if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        x = int(input().strip())
        solution(x)
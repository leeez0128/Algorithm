import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []

def BackTracking(N, M):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(1, N+1):
        # if i in result:
        #     continue
        # else:
            result.append(i)
            BackTracking(N, M)
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    BackTracking(N, M)
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []

def BackTracking(N, M, start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N+1):
        if i in result:
            continue
        else:
            result.append(i)
            BackTracking(N, M, i)
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    BackTracking(N, M, 1)
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []

def BackTracking(seq, M):
    if len(result) == M:
        print(*result)
        return
    
    for num in seq:
        if num in result:
            continue
        else:
            result.append(num)
            BackTracking(seq, M)
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    seq = sorted(list(map(int, input().strip().split())))
    BackTracking(seq, M)

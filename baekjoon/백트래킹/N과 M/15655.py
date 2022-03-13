import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []


def BackTracking(seq, M, start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start, len(seq)):
        if seq[i] in result:
            continue
        else:
            result.append(seq[i])
            BackTracking(seq, M, i)
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    seq = sorted(list(map(int, input().strip().split())))
    BackTracking(seq, M, 0)

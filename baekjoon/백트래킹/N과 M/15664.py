import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []


def BackTracking(seq, M, start, use):
    if len(result) == M:
        print(*result)
        return
    
    duplicate = 0
    for num in range(start, len(seq)):
        if not use[num] and duplicate != seq[num]:
            result.append(seq[num])
            use[num] = True
            duplicate = seq[num]
            BackTracking(seq, M, num, use)
            result.pop()
            use[num] = False


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    seq = sorted(list(map(int, input().strip().split())))
    use = [False]*N
    BackTracking(seq, M, 0, use)

import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []


def BackTracking(seq, M):
    if len(result) == M:
        print(*result)
        return

    duplicate = 0
    for num in range(len(seq)):
        if duplicate != seq[num]:
            result.append(seq[num])
            BackTracking(seq, M)
            duplicate = seq[num]
            result.pop()


if __name__ == '__main__':
    N, M = map(int,input().strip().split())
    seq = sorted(list(map(int, input().strip().split())))
    BackTracking(seq, M)

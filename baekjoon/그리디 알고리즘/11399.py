import sys
input = sys.stdin.readline


def solution(N, times):
    times = sorted(times)
    for i in range(N-1):
        times[i+1] += times[i]

    print(sum(times))


if __name__ == '__main__':
    N = int(input().strip())
    times = list(map(int, input().strip().split()))
    solution(N, times)

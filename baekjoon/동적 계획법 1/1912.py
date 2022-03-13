import sys
input = sys.stdin.readline


def solution(n, seq):
    for i in range(1, n):
        seq[i] = max(seq[i], seq[i-1]+seq[i])

    print(max(seq))    


if __name__ == '__main__':
    n = int(input().strip())
    seq = list(map(int, input().strip().split()))
    solution(n, seq)

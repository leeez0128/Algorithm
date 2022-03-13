import sys
input = sys.stdin.readline


def solution(N, X, seq):
    for i in range(N):
        if(seq[i] < X):
            print(seq[i], end=" ")


if __name__ == "__main__":
    N, X = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))
    solution(N, X, seq)

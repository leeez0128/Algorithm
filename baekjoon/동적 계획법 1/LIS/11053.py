import sys
input = sys.stdin.readline


def solution(N, A):
    longest_seq = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                longest_seq[i] = max(longest_seq[i], longest_seq[j]+1)
            
    print(max(longest_seq))


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    solution(N, A)

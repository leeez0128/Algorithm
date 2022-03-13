import sys
input = sys.stdin.readline


def solution(N, seq):
    maxi = seq[0]
    mini = seq[0]
    
    for i in range(N):
        if(maxi < seq[i]):
            maxi = seq[i]
        if(mini > seq[i]):
            mini = seq[i]

    print(mini, maxi)


if __name__ == '__main__':
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))
    solution(N, seq)

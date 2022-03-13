import sys
input = sys.stdin.readline


def solution(N, K):
    seq = [i+1 for i in range(N)]
    result = []
    tmp = K - 1

    while seq:
        if len(seq) <= tmp:
            tmp = tmp % len(seq)
        
        result.append(seq.pop(tmp))
        tmp += (K - 1)
        
    print("<", ", ".join(str(num) for num in result), ">", sep="")

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N, K)

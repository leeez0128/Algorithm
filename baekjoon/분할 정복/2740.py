import sys
input = sys.stdin.readline


def solution(N, M, K, A, B):
    result = [[0 for _ in range(K)] for _ in range(N)]
    
    for n in range(N):
        for k in range(K):
            for m in range(M):
                result[n][k] += A[n][m] * B[m][k]
    
    for row in result:
        print(*row)
        

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().strip().split())))
            
    M, K = map(int, input().strip().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().strip().split())))
    solution(N, M, K, A, B)
